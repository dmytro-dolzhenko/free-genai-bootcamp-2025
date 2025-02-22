import streamlit as st
import chromadb
import json
import sys
import os
from typing import List, Dict
import boto3
from uuid import uuid4
import random

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from transcript_analyzer import TranscriptAnalyzer
from audio_generator import AudioGenerator

class JLPTPracticeApp:
    def __init__(self):
        try:
            # Update path to point to backend's chroma_db
            self.chroma_client = chromadb.PersistentClient(
                path=os.path.join(os.path.dirname(__file__), '..', 'backend', 'chroma_db')
            )
            # Try to get or create the collection
            self.collection = self.chroma_client.get_or_create_collection("japanese_lessons")
        except Exception as e:
            st.error(f"Error initializing ChromaDB: {str(e)}")
            self.chroma_client = None
            self.collection = None
        
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name='eu-west-1'
        )
        self.analyzer = TranscriptAnalyzer(region_name="eu-west-1", model_id="mistral.mistral-large-2402-v1:0")
        self.audio_generator = AudioGenerator(region_name="eu-west-1")
        
    def get_categories(self) -> List[str]:
        """Get unique categories from ChromaDB"""
        if not self.collection:
            return []
        
        try:
            result = self.collection.get(
                include=['metadatas'],
            )
            
            # Extract unique topics from metadata
            topics = set()
            for metadata in result['metadatas']:
                if 'topic' in metadata:
                    topics.add(metadata['topic'])
            
            return sorted(list(topics))
        except Exception as e:
            st.error(f"Error getting categories: {str(e)}")
            return []

    def get_section_patterns(self, topic: str) -> List[Dict]:
        """Get question patterns for the selected topic"""
        if not self.collection:
            return []
            
        try:
            # Define default patterns at the start of the method
            default_patterns = [
                "Listen to a task-based conversation and answer questions",
                "Listen to a quick response dialogue and select the appropriate reply",
                "Listen to a conversation between two people and answer questions",
                "Listen to an announcement or explanation and answer questions"
            ]
            
            result = self.collection.get(
                where={
                    "$and": [
                        {"topic": {"$eq": topic}},
                        {"content_type": {"$eq": "pattern"}}
                    ]
                },
                include=['documents', 'metadatas']
            )
            
            # Define the 4 standard JLPT N5 listening sections
            sections = [
                {"name": "Section 1: Task-based Comprehension", "patterns": []},
                {"name": "Section 2: Quick Response", "patterns": []},
                {"name": "Section 3: Short Conversations", "patterns": []},
                {"name": "Section 4: Information/Monologue", "patterns": []}
            ]
            
            # Get all available patterns
            all_patterns = []
            for doc, meta in zip(result['documents'], result['metadatas']):
                patterns = doc.split('Patterns:\n')[1].split('\n') if 'Patterns:\n' in doc else []
                all_patterns.extend([p for p in patterns if p.strip()])  # Only add non-empty patterns
            
            # If no patterns found, use default patterns
            if not all_patterns:
                all_patterns = default_patterns.copy()
            
            # Distribute patterns evenly across sections
            patterns_per_section = max(1, len(all_patterns) // 4)
            for i, section in enumerate(sections):
                start_idx = i * patterns_per_section
                end_idx = start_idx + patterns_per_section if i < 3 else len(all_patterns)
                section_patterns = all_patterns[start_idx:end_idx]
                
                # Ensure each section has at least one pattern
                if not section_patterns:
                    section_patterns = [default_patterns[i]]
                
                section["patterns"] = section_patterns
            
            return sections
            
        except Exception as e:
            st.error(f"Error getting patterns: {str(e)}")
            return []

    def generate_similar_question(self, patterns: List[str], topic: str, section_name: str = "") -> Dict:
        """Generate a similar question based on patterns."""
        try:
            # Get similar patterns from the collection
            results = self.collection.query(
                query_texts=[f"pattern:{pattern}" for pattern in patterns],
                n_results=5,
                where={"topic": topic} if topic else None
            )
            
            if not results or not results['documents']:
                st.error("No similar patterns found")
                return None
            
            # Select a random pattern from results
            pattern_idx = random.randint(0, len(results['documents'][0]) - 1)
            pattern = results['documents'][0][pattern_idx]
            
            # Generate prompt for the LLM
            prompt = f"""You are a JLPT question generator. Create a new listening comprehension question in JSON format.
            Follow this pattern exactly: {pattern}
            Topic: {topic}
            Section: {section_name}

            Return ONLY valid JSON with no additional text. Use ONLY these character names consistently:
            - 田中先生 (Tanaka Sensei) for teacher/announcer
            - 田中太郎 (Tanaka Taro) for male student/customer
            - 山本さくら (Yamamoto Sakura) for female student/customer

            Following this structure:

            For Section 1 (Task-based Comprehension):
            {{
                "conversation": [
                    {{"speaker": "田中先生 (Tanaka Sensei)", "text": "日本語のタスクや状況の説明"}},
                    {{"speaker": "田中太郎 (Tanaka Taro)", "text": "タスクについての質問"}},
                    {{"speaker": "田中先生 (Tanaka Sensei)", "text": "選択肢の説明"}}
                ],
                "question_text": "状況に合った適切な行動や答えを選んでください",
                "answer_options": ["図書館で本を借りる", "先生に質問する", "友達と相談する", "家で勉強する"],
                "correct_answer": "図書館で本を借りる",
                "explanation": "Explanation in English"
            }}

            For Sections 2-3 (Dialog/Conversation):
            {{
                "conversation": [
                    {{"speaker": "田中太郎 (Tanaka Taro)", "text": "日本語の会話"}},
                    {{"speaker": "山本さくら (Yamamoto Sakura)", "text": "日本語の返事"}}
                ],
                "question_text": "日本語の質問",
                "answer_options": ["はい、そうです", "いいえ、違います", "わかりません", "もう一度お願いします"],
                "correct_answer": "はい、そうです",
                "explanation": "Explanation in English"
            }}

            For Section 4 (Information/Monologue):
            {{
                "monologue": {{
                    "speaker": "田中先生 (Tanaka Sensei)",
                    "text": "日本語のお知らせや説明"
                }},
                "question_text": "お知らせの内容について質問",
                "answer_options": ["午前十時から", "図書館で", "三年生の教室で", "来週の月曜日に"],
                "correct_answer": "図書館で",
                "explanation": "Explanation in English"
            }}"""
            
            # Call Bedrock to generate the question
            response = self.analyzer.analyze_transcript(prompt)
            
            try:
                # Parse the response
                question = json.loads(response)
                
                # Validate required fields
                required_fields = ['question_text', 'answer_options', 'correct_answer', 'explanation']
                if all(field in question for field in required_fields):
                    if "Section 4" in section_name:
                        # Handle Section 4 as monologue
                        if not isinstance(question.get('monologue'), dict) or \
                           'speaker' not in question['monologue'] or \
                           'text' not in question['monologue']:
                            st.error("Invalid monologue structure")
                            return None
                        try:
                            audio_path = self.audio_generator.generate_conversation_audio({
                                "monologue": question["monologue"]
                            })
                            question["audio_path"] = audio_path
                        except Exception as e:
                            st.warning(f"Audio generation failed: {str(e)}")
                        return question
                    else:
                        # Handle other sections as conversations
                        if not isinstance(question.get('conversation'), list) or \
                           not all('speaker' in line and 'text' in line for line in question['conversation']):
                            st.error("Invalid conversation structure")
                            return None
                        try:
                            audio_path = self.audio_generator.generate_conversation_audio({
                                "conversation": question["conversation"]
                            })
                            question["audio_path"] = audio_path
                        except Exception as e:
                            st.warning(f"Audio generation failed: {str(e)}")
                        return question
                else:
                    st.error("Generated question is missing required fields")
                    return None
                    
            except json.JSONDecodeError:
                st.error("Invalid JSON response from LLM")
                st.write("Response:", response)  # Debug print
                return None
            
        except Exception as e:
            st.error(f"Error generating question: {str(e)}")
            return None

    def run(self):
        st.title("JLPT Practice Questions")
        
        # Get categories
        categories = self.get_categories()
        if not categories:
            st.error("No categories found in the database")
            return
            
        # Category selection
        selected_category = st.selectbox(
            "Select a category:",
            categories
        )
        
        if selected_category:
            # Get patterns for the category
            patterns = self.get_section_patterns(selected_category)
            
            if patterns:
                st.subheader("Practice Questions")
                
                # Create section tabs with both English and Japanese names
                section_names = [p["name"] for p in patterns]
                tabs = st.tabs(section_names)
                
                for tab_idx, (tab, pattern_group) in enumerate(zip(tabs, patterns)):
                    with tab:
                        # Generate a question using a random pattern
                        if pattern_group['patterns']:
                            pattern = pattern_group['patterns'][0]  # Use first pattern if available
                        else:
                            # Use a default pattern based on the section
                            default_patterns = {
                                "Section 1": "Listen to a task-based conversation and answer questions",
                                "Section 2": "Listen to a quick response dialogue and select the appropriate reply",
                                "Section 3": "Listen to a conversation between two people and answer questions",
                                "Section 4": "Listen to an announcement or explanation and answer questions"
                            }
                            pattern = default_patterns.get(pattern_group['name'].split(":")[0], "Listen and answer questions")
                        
                        # Use section number for tab_id
                        tab_id = f"tab_section_{tab_idx + 1}"  # Fixed: Use tab_idx instead of undefined tab_id
                        
                        if tab_id not in st.session_state:
                            question = self.generate_similar_question(
                                pattern_group['patterns'], 
                                selected_category,
                                section_name=pattern_group['name']
                            )
                            st.session_state[tab_id] = question
                        
                        question = st.session_state[tab_id]
                        
                        if question:
                            if "monologue" in question:
                                # Display monologue
                                st.subheader("Monologue")
                                st.markdown(f"**{question['monologue']['speaker']}**:")
                                st.markdown(question['monologue']['text'])
                            else:
                                # Display conversation
                                st.subheader("Conversation")
                                for line in question['conversation']:
                                    st.markdown(f"**{line['speaker']}**: {line['text']}")
                            
                            # Display audio player if audio was generated
                            if "audio_path" in question:
                                st.audio(question["audio_path"])
                            
                            # Display question
                            st.subheader("Question")  # Changed from 問題
                            st.markdown(question['question_text'])
                            
                            # Create unique keys for radio buttons and buttons
                            radio_key = f"radio_{tab_id}_{hash(question['question_text'])}"
                            check_key = f"check_{tab_id}_{hash(question['question_text'])}"
                            new_key = f"new_{tab_id}_{hash(question['question_text'])}"
                            
                            # Radio buttons for answer options
                            st.markdown("**Select your answer:**")  # Changed from 答えを選んでください
                            answer = st.radio(
                                "",  # Empty label since we added the header above
                                question['answer_options'],
                                key=radio_key
                            )
                            
                            # Check answer button
                            if st.button("Check Answer", key=check_key):  # Changed from 答え合わせ
                                if answer == question['correct_answer']:
                                    st.success("Correct! 🎉")  # Changed from 正解
                                else:
                                    st.error(f"Incorrect. The correct answer is: {question['correct_answer']}")  # Changed from 不正解
                                st.info(f"Explanation: {question['explanation']}")
                            
                            # Generate new question button
                            if st.button("New Question", key=new_key):
                                # Use the same tab_id that we used for initialization
                                # Clear the old question
                                st.session_state.pop(tab_id, None)  # Use tab_id directly, not state_key
                                # Generate new question
                                st.session_state[tab_id] = self.generate_similar_question(
                                    pattern_group['patterns'], 
                                    selected_category, 
                                    section_name=pattern_group['name']
                                )
                                st.rerun()

if __name__ == "__main__":
    app = JLPTPracticeApp()
    app.run() 