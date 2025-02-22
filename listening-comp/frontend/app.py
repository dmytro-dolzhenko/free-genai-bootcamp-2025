import streamlit as st
import chromadb
import json
import sys
import os
from typing import List, Dict
import boto3
from uuid import uuid4

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from transcript_analyzer import TranscriptAnalyzer

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

    def get_similar_questions(self, pattern: str, topic: str, n_results: int = 3) -> List[Dict]:
        """Get similar questions from ChromaDB using pattern matching"""
        if not self.collection:
            return []
        
        try:
            # Create query text combining pattern and topic
            query_text = f"Pattern: {pattern}\nTopic: {topic}"
            
            # Search for similar questions
            results = self.collection.query(
                query_texts=[query_text],
                where={
                    "$and": [
                        {"content_type": {"$eq": "question"}},
                        {"topic": {"$eq": topic}}
                    ]
                },
                n_results=n_results,
                include=['documents', 'metadatas']
            )
            
            similar_questions = []
            for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
                # Parse the document text to extract question components
                lines = doc.split('\n')
                question_dict = {
                    'question_text': next((l.replace('Question: ', '') for l in lines if l.startswith('Question: ')), ''),
                    'context': next((l.replace('Context: ', '') for l in lines if l.startswith('Context: ')), ''),
                    'pattern': meta.get('pattern', pattern),
                    'answer_options': [l.strip() for l in lines if l.startswith('Options:')][0].split('\n'),
                    'correct_answer': next((l.replace('Correct Answer: ', '') for l in lines if l.startswith('Correct Answer: ')), '')
                }
                similar_questions.append(question_dict)
            
            return similar_questions
        except Exception as e:
            st.error(f"Error getting similar questions: {str(e)}")
            return []

    def generate_similar_question(self, pattern: str, topic: str, section_name: str = "") -> Dict:
        """Generate a new question using pattern and similar examples"""
        try:
            # Get similar questions from ChromaDB
            similar_questions = self.get_similar_questions(pattern, topic)
            
            # Create examples string
            examples = ""
            if similar_questions:
                examples = "Here are some example questions with this pattern:\n"
                for i, q in enumerate(similar_questions, 1):
                    examples += f"""
                    Example {i}:
                    Context: {q['context']}
                    Question: {q['question_text']}
                    Options: {', '.join(q['answer_options'])}
                    Correct Answer: {q['correct_answer']}
                    """
            
            # Create base prompt
            base_prompt = f"""
            Generate a new JLPT practice question similar to this pattern: {pattern}
            Topic: {topic}
            Section: {section_name}
            
            {examples}
            """
            
            # Add section-specific JSON structure
            if "Information/Monologue" in section_name:
                json_structure = """
                {
                    "monologue": {
                        "speaker": "田中太郎 (Tanaka Taro)",
                        "text": "A longer monologue in Japanese about a topic, announcement, or explanation"
                    },
                    "question_text": "Japanese question text about the monologue",
                    "answer_options": [
                        "Japanese option 1",
                        "Japanese option 2",
                        "Japanese option 3",
                        "Japanese option 4"
                    ],
                    "correct_answer": "The correct Japanese option",
                    "explanation": "Explanation in English why this is the correct answer"
                }
                """
            elif "Quick Response" in section_name:
                json_structure = """
                {
                    "conversation": [
                        {"speaker": "田中太郎 (Tanaka Taro)", "text": "Short question in Japanese"},
                        {"speaker": "山本さくら (Yamamoto Sakura)", "text": "Quick response in Japanese"}
                    ],
                    "question_text": "Japanese question about the quick response",
                    "answer_options": [
                        "Japanese option 1",
                        "Japanese option 2",
                        "Japanese option 3",
                        "Japanese option 4"
                    ],
                    "correct_answer": "The correct Japanese option",
                    "explanation": "Explanation in English why this is the correct answer"
                }
                """
            else:
                json_structure = """
                {
                    "conversation": [
                        {"speaker": "田中太郎 (Tanaka Taro)", "text": "First line of dialogue in Japanese"},
                        {"speaker": "山本さくら (Yamamoto Sakura)", "text": "Second line of dialogue in Japanese"},
                        {"speaker": "田中太郎 (Tanaka Taro)", "text": "Third line of dialogue in Japanese"},
                        {"speaker": "山本さくら (Yamamoto Sakura)", "text": "Fourth line of dialogue in Japanese"}
                    ],
                    "question_text": "Japanese question text about the conversation",
                    "answer_options": [
                        "Japanese option 1",
                        "Japanese option 2",
                        "Japanese option 3",
                        "Japanese option 4"
                    ],
                    "correct_answer": "The correct Japanese option",
                    "explanation": "Explanation in English why this is the correct answer"
                }
                """
            
            # Add names list and requirements
            prompt = base_prompt + """
            Use random names from these common Japanese names (include both kanji and romaji):
            Male names:
            - 田中太郎 (Tanaka Taro)
            - 鈴木一郎 (Suzuki Ichiro)
            - 佐藤健 (Sato Ken)
            - 山田翔太 (Yamada Shota)
            - 中村勇気 (Nakamura Yuki)
            
            Female names:
            - 山本さくら (Yamamoto Sakura)
            - 高橋美咲 (Takahashi Misaki)
            - 渡辺花子 (Watanabe Hanako)
            - 小林愛 (Kobayashi Ai)
            - 伊藤優子 (Ito Yuko)

            Return a valid JSON object with exactly this structure:
            """ + json_structure + """

            Important:
            1. Make sure to return VALID JSON with correct formatting and escaping
            2. Do not include any additional text before or after the JSON
            3. Use proper JSON syntax with double quotes for strings
            4. Use appropriate JLPT N5 level vocabulary and grammar
            5. Choose appropriate names from the provided lists
            6. For Section 2 (Quick Response), use short question-answer exchanges
            7. For Section 3, ensure natural dialogue flow
            8. For Section 4 (Monologue), focus on announcements or explanations
            """
            
            try:
                response = self.analyzer._invoke_bedrock(prompt)
                if isinstance(response, dict) and 'choices' in response:
                    response = response['choices'][0]['message']['content']
                
                # Clean up response
                response = response.strip()
                if response.startswith('```json'):
                    response = response[7:]
                if response.endswith('```'):
                    response = response[:-3]
                response = response.strip()
                
                # Parse JSON with error handling
                try:
                    question = json.loads(response)
                    
                    # Define required fields based on section type
                    if "Information/Monologue" in section_name:
                        required_fields = ['monologue', 'question_text', 'answer_options', 'correct_answer', 'explanation']
                    else:
                        required_fields = ['conversation', 'question_text', 'answer_options', 'correct_answer', 'explanation']
                    
                    # Validate required fields
                    if all(field in question for field in required_fields):
                        # Additional validation for conversation/monologue structure
                        if "Information/Monologue" in section_name:
                            if not isinstance(question['monologue'], dict) or \
                               'speaker' not in question['monologue'] or \
                               'text' not in question['monologue']:
                                st.error("Invalid monologue structure")
                                return None
                        else:
                            if not isinstance(question['conversation'], list) or \
                               not all('speaker' in line and 'text' in line for line in question['conversation']):
                                st.error("Invalid conversation structure")
                                return None
                        
                        # Validate answer options
                        if not isinstance(question['answer_options'], list) or \
                           len(question['answer_options']) < 2:
                            st.error("Invalid answer options")
                            return None
                        
                        return question
                    else:
                        missing = [f for f in required_fields if f not in question]
                        st.error(f"Generated question is missing required fields: {', '.join(missing)}")
                        st.code(response)  # Display the problematic response
                        return None
                    
                except json.JSONDecodeError as e:
                    st.error(f"Invalid JSON response: {str(e)}")
                    st.code(response)  # Display the problematic response
                    return None
                    
            except Exception as e:
                st.error(f"Error in API response: {str(e)}")
                st.code(prompt)  # Display the prompt that caused the error
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
                                pattern, 
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
                            if st.button("New Question", key=new_key):  # Changed from 新しい問題
                                st.session_state[tab_id] = self.generate_similar_question(
                                    pattern, selected_category, pattern_group['name']
                                )
                                st.rerun()

if __name__ == "__main__":
    app = JLPTPracticeApp()
    app.run() 