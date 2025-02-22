## SpecStory

## Transcript Analysis and Question Generation (2/21/2025, 10:48:33 PM)

_**User**_

@transcript_analyzer.py 
So the idea is that I am going to have a frontend which will allow a user to select a topic among available ones (based on transcript data) and then similar questions for each sections from the transcripts should be generated and shown to the user. Each questions should have multi-choice answer options and one correct option. To be able to generate similar questions I need to store information from transcripts in the vector store in accessible format. Could you please help me to modify the prompt to get the best results in the right format. Formatted output should be stored within files ready to be loaded into Vector store.


---

_**Assistant**_

I'll help you modify the TranscriptAnalyzer to better structure the data for vector storage and question generation. We'll update the prompt and add functionality to format the output in a way that's optimal for vector storage.

Here's how we can modify the file:

```python:backend/transcript_analyzer.py
# ... existing code ...

    def _invoke_bedrock(self, prompt: str) -> str:
        # ... existing code ...

    def analyze_transcript(self, filename: str) -> Dict:
        """
        Analyze a transcript file to extract key information in a format suitable for vector storage.
        
        Args:
            filename (str): Name of transcript file
            
        Returns:
            Dict: Analyzed information including topic, sections, and structured question data
        """
        transcript = self._read_transcript(filename)
        
        analysis_prompt = f"""
        Analyze this Japanese language test transcript and extract structured information. Format the response as a JSON object that captures the essential elements for generating similar questions. Focus on the patterns and structures that make each question type unique.

        Return a JSON object with this structure:
        {{
            "topic": {{
                "main": "string (e.g., JLPT N5 Grammar)",
                "subtopic": "string (e.g., Particle Usage)",
                "difficulty": "string (N5/N4/N3/N2/N1)"
            }},
            "sections": [
                {{
                    "name": "string (e.g., Reading Comprehension)",
                    "question_type": "string (e.g., particle-selection, vocabulary-usage)",
                    "questions": [
                        {{
                            "question_text": "string",
                            "question_pattern": "string (describe the pattern this question follows)",
                            "context": "string (if applicable)",
                            "options": [
                                {{
                                    "text": "string",
                                    "explanation": "string (why this option is correct/incorrect)"
                                }}
                            ],
                            "correct_answer": "string",
                            "grammar_points": ["string"],
                            "vocabulary_focus": ["string"],
                            "explanation": "string (detailed explanation of the correct answer)",
                            "similar_question_template": "string (template for generating similar questions)"
                        }}
                    ],
                    "section_characteristics": {{
                        "common_patterns": ["string"],
                        "key_grammar_points": ["string"],
                        "typical_vocabulary_types": ["string"]
                    }}
                }}
            ]
        }}

        For each question, provide clear patterns and templates that can be used to generate similar questions.
        Include detailed explanations for why answers are correct or incorrect.
        Identify common patterns within each section that can be used for question generation.

        Transcript:
        {transcript}
        """
        
        try:
            response = self._invoke_bedrock(analysis_prompt)
            print("Model response:", response)  # Debug logging
            
            # Clean and parse JSON response
            json_str = response.strip()
            if json_str.startswith("```json"):
                json_str = json_str[7:]
            if json_str.endswith("```"):
                json_str = json_str[:-3]
            
            analysis_result = json.loads(json_str)
            
            # Format the data for vector storage
            vectorized_data = self._format_for_vector_storage(analysis_result)
            
            return vectorized_data
        except json.JSONDecodeError as e:
            return {
                "error": "Failed to parse analysis response",
                "raw_response": response,
                "error_details": str(e)
            }
        except Exception as e:
            return {
                "error": f"Analysis failed: {str(e)}",
                "raw_response": response if 'response' in locals() else None
            }

    def _format_for_vector_storage(self, analysis_result: Dict) -> Dict:
        """
        Format the analysis results into documents suitable for vector storage.
        
        Args:
            analysis_result (Dict): Raw analysis results
            
        Returns:
            Dict: Formatted data ready for vector storage
        """
        vectorized_data = {
            "topic_info": analysis_result["topic"],
            "question_documents": [],
            "pattern_documents": []
        }
        
        # Create individual documents for each question
        for section in analysis_result["sections"]:
            for question in section["questions"]:
                question_doc = {
                    "content_type": "question",
                    "topic": analysis_result["topic"]["main"],
                    "subtopic": analysis_result["topic"]["subtopic"],
                    "section_name": section["name"],
                    "question_type": section["question_type"],
                    "question_text": question["question_text"],
                    "context": question["context"],
                    "pattern": question["question_pattern"],
                    "options": question["options"],
                    "correct_answer": question["correct_answer"],
                    "explanation": question["explanation"],
                    "metadata": {
                        "grammar_points": question["grammar_points"],
                        "vocabulary_focus": question["vocabulary_focus"],
                        "difficulty": analysis_result["topic"]["difficulty"]
                    }
                }
                vectorized_data["question_documents"].append(question_doc)
            
            # Create pattern documents for each section
            pattern_doc = {
                "content_type": "pattern",
                "section_name": section["name"],
                "question_type": section["question_type"],
                "common_patterns": section["section_characteristics"]["common_patterns"],
                "key_grammar_points": section["section_characteristics"]["key_grammar_points"],
                "typical_vocabulary_types": section["section_characteristics"]["typical_vocabulary_types"],
                "metadata": {
                    "topic": analysis_result["topic"]["main"],
                    "difficulty": analysis_result["topic"]["difficulty"]
                }
            }
            vectorized_data["pattern_documents"].append(pattern_doc)
        
        return vectorized_data

    # ... rest of existing code ...
```

This updated version makes several important improvements:

1. The prompt now requests more structured information about question patterns and templates for generating similar questions.

2. Added detailed metadata about grammar points and vocabulary focus for each question.

3. Introduced a new `_format_for_vector_storage` method that transforms the analysis results into documents suitable for vector storage:
   - Question documents that contain individual questions with all their metadata
   - Pattern documents that capture common patterns and characteristics of each section

4. Each document includes rich metadata that can be used for filtering and searching.

5. The structured output makes it easier to:
   - Generate similar questions using the patterns and templates
   - Search for questions by topic, grammar point, or vocabulary
   - Filter questions by difficulty level
   - Group related questions by pattern or section type

To use this updated version:

1. Store the question documents in your vector store with their text content (question text + context) as the vector embedding
2. Store the pattern documents separately to help with question generation
3. Use the metadata for filtering and organizing the questions in your frontend

The frontend can then:
1. Allow users to select topics and subtopics
2. Filter questions by difficulty level
3. Generate similar questions using the patterns and templates
4. Show detailed explanations for each answer option

Would you like me to add any additional functionality or modify the structure further?

---

_**User**_

I don't need subtopics, difficulty level, etc. I just need topic and I need questions, available answer options and correct answer. Sections are also important as I want to be able to have similar questions for each section.

---

_**Assistant**_

I'll help simplify the structure to focus on just the essential elements you need.

```python:backend/transcript_analyzer.py
    def analyze_transcript(self, filename: str) -> Dict:
        """
        Analyze a transcript file to extract key information for question generation.
        
        Args:
            filename (str): Name of transcript file
            
        Returns:
            Dict: Analyzed information including topic, sections, and questions
        """
        transcript = self._read_transcript(filename)
        
        analysis_prompt = f"""
        Analyze this Japanese language test transcript and extract structured information. Focus on identifying question patterns within each section to enable generation of similar questions.

        Return a JSON object with this structure:
        {{
            "topic": "string (e.g., JLPT N5 Grammar)",
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

        Focus on capturing the essential structure of each question type to enable generation of similar questions.
        Make sure to identify clear patterns that can be used as templates.

        Transcript:
        {transcript}
        """
        
        try:
            response = self._invoke_bedrock(analysis_prompt)
            print("Model response:", response)  # Debug logging
            
            # Clean and parse JSON response
            json_str = response.strip()
            if json_str.startswith("```json"):
                json_str = json_str[7:]
            if json_str.endswith("```"):
                json_str = json_str[:-3]
            
            analysis_result = json.loads(json_str)
            
            # Format the data for vector storage
            vectorized_data = self._format_for_vector_storage(analysis_result)
            
            return vectorized_data
        except json.JSONDecodeError as e:
            return {
                "error": "Failed to parse analysis response",
                "raw_response": response,
                "error_details": str(e)
            }
        except Exception as e:
            return {
                "error": f"Analysis failed: {str(e)}",
                "raw_response": response if 'response' in locals() else None
            }

    def _format_for_vector_storage(self, analysis_result: Dict) -> Dict:
        """
        Format the analysis results into documents suitable for vector storage.
        
        Args:
            analysis_result (Dict): Raw analysis results
            
        Returns:
            Dict: Formatted data ready for vector storage
        """
        vectorized_data = {
            "topic": analysis_result["topic"],
            "question_documents": [],
            "pattern_documents": []
        }
        
        # Create individual documents for each question
        for section in analysis_result["sections"]:
            for question in section["questions"]:
                question_doc = {
                    "content_type": "question",
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
                "section_name": section["name"],
                "question_type": section["question_type"],
                "patterns": section["section_patterns"],
                "topic": analysis_result["topic"]
            }
            vectorized_data["pattern_documents"].append(pattern_doc)
        
        return vectorized_data
```

The key changes made:

1. Simplified the JSON structure to focus only on:
   - Topic
   - Sections with question types
   - Questions with their core components (text, options, correct answer)
   - Question patterns for generating similar questions

2. Removed extra metadata like difficulty levels, grammar points, and subtopics

3. Simplified the vector storage format to include only the essential fields needed for:
   - Question documents: containing the actual questions and their answers
   - Pattern documents: containing the patterns for generating similar questions

This structure will allow you to:
1. Organize questions by topic and section
2. Generate similar questions using the patterns
3. Present questions with their multiple-choice options
4. Check correct answers

The pattern information will be particularly useful when you want to generate new questions that follow the same structure as existing ones in each section.

---

_**User**_

Could you please save vectorized data into files under vectorized_data folder

---

_**Assistant**_

I'll help you add functionality to save the vectorized data into separate files in a vectorized_data folder.

```python:backend/transcript_analyzer.py
    def _format_for_vector_storage(self, analysis_result: Dict) -> Dict:
        """
        Format the analysis results into documents suitable for vector storage.
        
        Args:
            analysis_result (Dict): Raw analysis results
            
        Returns:
            Dict: Formatted data ready for vector storage
        """
        vectorized_data = {
            "topic": analysis_result["topic"],
            "question_documents": [],
            "pattern_documents": []
        }
        
        # Create individual documents for each question
        for section in analysis_result["sections"]:
            for question in section["questions"]:
                question_doc = {
                    "content_type": "question",
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
        # Create vectorized_data directory if it doesn't exist
        vector_dir = "vectorized_data"
        os.makedirs(vector_dir, exist_ok=True)
        
        # Sanitize topic name for filename
        topic_name = vectorized_data["topic"].lower().replace(" ", "_")
        
        # Save question documents
        questions_file = os.path.join(vector_dir, f"{topic_name}_questions.json")
        with open(questions_file, 'w', encoding='utf-8') as f:
            json.dump(vectorized_data["question_documents"], f, ensure_ascii=False, indent=2)
        
        # Save pattern documents
        patterns_file = os.path.join(vector_dir, f"{topic_name}_patterns.json")
        with open(patterns_file, 'w', encoding='utf-8') as f:
            json.dump(vectorized_data["pattern_documents"], f, ensure_ascii=False, indent=2)
        
        # Save topic metadata
        topic_file = os.path.join(vector_dir, f"{topic_name}_metadata.json")
        topic_metadata = {
            "topic": vectorized_data["topic"],
            "total_questions": len(vectorized_data["question_documents"]),
            "total_patterns": len(vectorized_data["pattern_documents"]),
            "sections": list(set(doc["section_name"] for doc in vectorized_data["question_documents"]))
        }
        with open(topic_file, 'w', encoding='utf-8') as f:
            json.dump(topic_metadata, f, ensure_ascii=False, indent=2)
```

The changes made:

1. Added a new `_save_vectorized_data` method that:
   - Creates a `vectorized_data` directory if it doesn't exist
   - Saves the data into three separate files for each topic:
     - `{topic_name}_questions.json`: Contains all question documents
     - `{topic_name}_patterns.json`: Contains all pattern documents
     - `{topic_name}_metadata.json`: Contains topic metadata and summary information

2. Modified `_format_for_vector_storage` to call the new save method

The files will be organized like this:
```
vectorized_data/
    jlpt_n5_grammar_questions.json
    jlpt_n5_grammar_patterns.json
    jlpt_n5_grammar_metadata.json
    jlpt_n5_vocabulary_questions.json
    jlpt_n5_vocabulary_patterns.json
    jlpt_n5_vocabulary_metadata.json
    ...
```

This structure makes it easy to:
1. Load questions and patterns for a specific topic
2. Get an overview of available topics and their contents
3. Access the vectorized data for your vector store implementation

Would you like me to add any additional functionality to the file saving system?

---

_**User**_

vectorised_data file names should be unique and have video id within it

---

_**Assistant**_

I'll modify the `_save_vectorized_data` method to include the video ID in the filenames. We'll extract the video ID from the transcript filename.

```python:backend/transcript_analyzer.py
    def analyze_transcript(self, filename: str) -> Dict:
        """
        Analyze a transcript file to extract key information for question generation.
        
        Args:
            filename (str): Name of transcript file
            
        Returns:
            Dict: Analyzed information including topic, sections, and questions
        """
        transcript = self._read_transcript(filename)
        
        # Extract video_id from filename (assuming filename format like "video_123.txt")
        video_id = os.path.splitext(filename)[0]  # Remove extension
        
        # ... rest of the existing analyze_transcript code ...
            
            analysis_result = json.loads(json_str)
            
            # Format the data for vector storage, passing video_id
            vectorized_data = self._format_for_vector_storage(analysis_result, video_id)
            
            return vectorized_data

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
        # Create vectorized_data directory if it doesn't exist
        vector_dir = "vectorized_data"
        os.makedirs(vector_dir, exist_ok=True)
        
        # Create unique filename using video_id and sanitized topic name
        video_id = vectorized_data["video_id"]
        topic_name = vectorized_data["topic"].lower().replace(" ", "_")
        base_filename = f"{video_id}_{topic_name}"
        
        # Save question documents
        questions_file = os.path.join(vector_dir, f"{base_filename}_questions.json")
        with open(questions_file, 'w', encoding='utf-8') as f:
            json.dump(vectorized_data["question_documents"], f, ensure_ascii=False, indent=2)
        
        # Save pattern documents
        patterns_file = os.path.join(vector_dir, f"{base_filename}_patterns.json")
        with open(patterns_file, 'w', encoding='utf-8') as f:
            

---



---

