import boto3
import json
import os
from typing import Dict, List, Optional

class TranscriptAnalyzer:
    def __init__(self, 
                 transcript_dir: str = "transcripts",
                 region_name: str = "us-east-1",
                 model_id: str = "mistral.mistral-large-2402-v1:0"):
        """
        Initialize TranscriptAnalyzer with AWS Bedrock client and transcript directory.
        
        Args:
            transcript_dir (str): Directory containing transcript files
            region_name (str): AWS region name for Bedrock
            model_id (str): Bedrock model ID to use for analysis
        """
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name
        )
        self.transcript_dir = transcript_dir
        self.model_id = model_id
        
    def _read_transcript(self, filename: str) -> str:
        """
        Read transcript file content.
        
        Args:
            filename (str): Name of transcript file
            
        Returns:
            str: Content of transcript file
        """
        filepath = os.path.join(self.transcript_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
            
    def _invoke_bedrock(self, prompt: str) -> str:
        """
        Invoke AWS Bedrock with given prompt using Mistral API.
        """
        body = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 4096,
            "temperature": 0,
            "top_p": 1
        })
        
        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=body
            )
            
            response_body = json.loads(response.get('body').read())
            
            # Debug logging
            print("Raw response:", response_body)
            
            if 'choices' in response_body:
                return response_body['choices'][0]['message']['content']
            elif 'messages' in response_body:
                return response_body['messages'][0]['content']
            else:
                raise ValueError(f"Unexpected response format: {response_body}")
            
        except Exception as e:
            print(f"Error in _invoke_bedrock: {str(e)}")
            raise

    def analyze_transcript(self, filename: str) -> Dict:
        """
        Analyze a transcript file to extract key information for question generation.
        
        Args:
            filename (str): Name of transcript file
            
        Returns:
            Dict: Analyzed information including topic, sections, and questions
        """
        try:
            transcript = self._read_transcript(filename)
            print(f"Read transcript file: {filename}")
            
            video_id = os.path.splitext(filename)[0]
            print(f"Extracted video_id: {video_id}")
            
            analysis_prompt = f"""
            Analyze this Japanese language test transcript and extract structured information.
            First, identify the specific conversation topic/subject matter (NOT the test type).

            Return a JSON object with this structure:
            {{
                "topic": "string (SPECIFIC conversation subject matter, e.g., 'Restaurant Orders', 'School Schedule', 'Shopping', 'Train Station', 'Weather', 'Daily Routine', etc. DO NOT put test types like 'Listening Comprehension' here)",
                "introduction": {{
                    "greeting": "string (opening greeting/introduction)",
                    "lesson_overview": "string (brief overview of what will be covered)",
                    "target_audience": "string (intended audience level)"
                }},
                "full_conversation": {{
                    "opening_segment": "string (first part of the test instructions/introduction)",
                    "example_segment": "string (example question and explanation if present)",
                    "main_segment": "string (main test content/questions)"
                }},
                "sections": [
                    {{
                        "name": "string (e.g., Reading Comprehension)",
                        "question_type": "string (e.g., particle-selection)",
                        "questions": [
                            {{
                                "question_text": "string",
                                "pattern": "string (describe how this type of question is structured)",
                                "context": "string (if applicable, for reading comprehension etc.)",
                                "answer_options": ["string"],
                                "correct_answer": "string",
                                "similar_question_template": "string (template showing how to create similar questions of this type)"
                            }}
                        ],
                        "section_patterns": ["string (common question patterns in this section)"]
                    }}
                ]
            }}

            Focus on capturing:
            1. The actual subject matter/topic of the conversations (e.g., 'Restaurant Orders', 'School Schedule')
            2. The complete introduction and greeting
            3. The main segments of the test content
            4. The essential structure of each question type to enable generation of similar questions
            5. Clear patterns that can be used as templates

            Transcript:
            {transcript}
            """
            
            response = self._invoke_bedrock(analysis_prompt)
            print(f"Got response from model for {filename}")
            
            try:
                # Clean and parse the response
                json_str = self._clean_json_string(response)
                analysis_result = json.loads(json_str)
                print(f"Successfully parsed JSON response for {filename}")
                
                # Validate required fields in analysis_result
                required_fields = ["topic", "introduction", "full_conversation", "sections"]
                missing_fields = [field for field in required_fields if field not in analysis_result]
                if missing_fields:
                    print(f"Warning: Missing required fields in analysis_result: {missing_fields}")
                    print(f"Analysis result keys: {list(analysis_result.keys())}")
                    print(f"Raw response: {response}")
                    return None
                
                # Format the data for vector storage, passing video_id
                print(f"Formatting data for vector storage for {filename}")
                vectorized_data = self._format_for_vector_storage(analysis_result, video_id)
                
                if vectorized_data:
                    print(f"Successfully created vectorized data for {filename}")
                    return vectorized_data
                else:
                    print(f"Failed to create vectorized data for {filename}")
                    return None
                
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON response for {filename}: {str(e)}")
                print(f"Raw response: {response}")
                return None
            
        except Exception as e:
            print(f"Error analyzing transcript {filename}: {str(e)}")
            return None

    def _clean_json_string(self, json_str: str) -> str:
        """
        Clean up JSON string by removing problematic characters and formatting.
        """
        if isinstance(json_str, dict):
            if 'choices' in json_str:
                json_str = json_str['choices'][0]['message']['content']
        
        # Remove any BOM or hidden characters
        json_str = json_str.encode().decode('utf-8-sig')
        
        # Remove any markdown formatting
        if json_str.startswith("```json"):
            json_str = json_str[7:]
        if json_str.endswith("```"):
            json_str = json_str[:-3]
        
        # Clean up whitespace and indentation
        lines = []
        for line in json_str.split('\n'):
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('//'):
                continue
            
            # Clean up ellipsis in text fields
            if '..."' in line:
                line = line.replace('..."', '"')
            if '... ' in line:
                line = line.replace('... ', '')
            if ' ...' in line:
                line = line.replace(' ...', '')
            
            lines.append(line)
        
        json_str = '\n'.join(lines)
        
        try:
            # Verify it's valid JSON by parsing and re-stringifying
            parsed = json.loads(json_str)
            return json.dumps(parsed, ensure_ascii=False)
        except json.JSONDecodeError as e:
            print(f"Error cleaning JSON: {str(e)}")
            print(f"Problematic JSON string: {json_str}")
            raise

    def _format_for_vector_storage(self, analysis_result: Dict, video_id: str) -> Dict:
        """
        Format the analysis results into documents suitable for vector storage.
        
        Args:
            analysis_result (Dict): Raw analysis results
            video_id (str): Unique identifier for the video/transcript
            
        Returns:
            Dict: Formatted data ready for vector storage
        """
        vectorized_data = {
            "video_id": video_id,
            "topic": analysis_result["topic"],
            "introduction": analysis_result["introduction"],
            "full_conversation": analysis_result["full_conversation"],
            "question_documents": [],
            "pattern_documents": []
        }
        
        # Create individual documents for each question
        for section in analysis_result["sections"]:
            for question in section["questions"]:
                question_doc = {
                    "content_type": "question",
                    "video_id": video_id,
                    "topic": analysis_result["topic"],
                    "section_name": section["name"],
                    "question_type": section["question_type"],
                    "question_text": question["question_text"],
                    "context": question["context"],
                    "pattern": question["pattern"],
                    "answer_options": question["answer_options"],
                    "correct_answer": question["correct_answer"]
                }
                vectorized_data["question_documents"].append(question_doc)
            
            # Create pattern documents for each section
            pattern_doc = {
                "content_type": "pattern",
                "video_id": video_id,
                "section_name": section["name"],
                "question_type": section["question_type"],
                "patterns": section["section_patterns"],
                "topic": analysis_result["topic"]
            }
            vectorized_data["pattern_documents"].append(pattern_doc)
        
        # Save the vectorized data to files
        self._save_vectorized_data(vectorized_data)
        
        return vectorized_data

    def _save_vectorized_data(self, vectorized_data: Dict):
        """
        Save vectorized data into separate files in the vectorized_data folder.
        
        Args:
            vectorized_data (Dict): Formatted vectorized data
        """
        try:
            # Validate required fields
            required_fields = ["video_id", "topic", "introduction", "full_conversation", 
                             "question_documents", "pattern_documents"]
            missing_fields = [field for field in required_fields if field not in vectorized_data]
            if missing_fields:
                print(f"Warning: Missing required fields in vectorized_data: {missing_fields}")
                return

            # Create vectorized_data directory if it doesn't exist
            vector_dir = "vectorized_data"
            os.makedirs(vector_dir, exist_ok=True)
            
            # Create unique filename using video_id and sanitized topic name
            video_id = vectorized_data["video_id"]
            topic_name = vectorized_data["topic"].lower().replace(" ", "_")
            base_filename = f"{video_id}_{topic_name}"
            
            print(f"Saving vectorized data for video {video_id}")
            
            # Save question documents
            questions_file = os.path.join(vector_dir, f"{base_filename}_questions.json")
            with open(questions_file, 'w', encoding='utf-8') as f:
                json.dump(vectorized_data["question_documents"], f, ensure_ascii=False, indent=2)
            print(f"Saved {len(vectorized_data['question_documents'])} questions to {questions_file}")
            
            # Save pattern documents
            patterns_file = os.path.join(vector_dir, f"{base_filename}_patterns.json")
            with open(patterns_file, 'w', encoding='utf-8') as f:
                json.dump(vectorized_data["pattern_documents"], f, ensure_ascii=False, indent=2)
            print(f"Saved {len(vectorized_data['pattern_documents'])} patterns to {patterns_file}")
            
            # Save topic metadata with introduction and conversation
            topic_file = os.path.join(vector_dir, f"{base_filename}_metadata.json")
            topic_metadata = {
                "video_id": video_id,
                "topic": vectorized_data["topic"],
                "introduction": vectorized_data["introduction"],
                "full_conversation": vectorized_data["full_conversation"],
                "total_questions": len(vectorized_data["question_documents"]),
                "total_patterns": len(vectorized_data["pattern_documents"]),
                "sections": list(set(doc["section_name"] for doc in vectorized_data["question_documents"]))
            }
            with open(topic_file, 'w', encoding='utf-8') as f:
                json.dump(topic_metadata, f, ensure_ascii=False, indent=2)
            print(f"Saved metadata with introduction and conversation to {topic_file}")

            # Verify files were created
            for filepath in [questions_file, patterns_file, topic_file]:
                if not os.path.exists(filepath):
                    print(f"Warning: Failed to verify file creation: {filepath}")
                else:
                    file_size = os.path.getsize(filepath)
                    print(f"Verified file {filepath} (size: {file_size} bytes)")

        except Exception as e:
            print(f"Error saving vectorized data: {str(e)}")
            raise

    def analyze_all_transcripts(self) -> List[Dict]:
        """
        Analyze all transcript files in the transcripts directory.
        
        Returns:
            List[Dict]: List of analysis results for each transcript
        """
        results = []
        transcript_dir = "transcripts"
        
        # Create vectorized_data directory if it doesn't exist
        os.makedirs("vectorized_data", exist_ok=True)
        
        print(f"Looking for transcript files in {transcript_dir}")
        
        for filename in os.listdir(transcript_dir):
            if filename.endswith(".txt"):
                print(f"Processing transcript: {filename}")
                try:
                    result = self.analyze_transcript(filename)
                    if result:
                        results.append(result)
                        print(f"Successfully analyzed {filename}")
                    else:
                        print(f"No results generated for {filename}")
                except Exception as e:
                    print(f"Error analyzing {filename}: {str(e)}")
                    continue
        
        print(f"Analyzed {len(results)} transcripts successfully")
        return results

    def save_analysis(self, analysis_results: Dict, output_file: str = "transcript_analysis.json"):
        """
        Save analysis results to a JSON file.
        
        Args:
            analysis_results (Dict): Analysis results to save
            output_file (str): Output file path
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_results, f, ensure_ascii=False, indent=2) 