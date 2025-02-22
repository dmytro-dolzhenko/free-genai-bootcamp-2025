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

    def analyze_transcript(self, prompt: str) -> str:
        """
        Analyze transcript using AWS Bedrock.
        
        Args:
            prompt (str): The prompt to send to the model
            
        Returns:
            str: The model's response
        """
        try:
            # Prepare the request body for Mistral model
            body = json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 2000,
                "temperature": 0.7,
                "top_p": 0.9
            })
            
            # Call Bedrock
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=body
            )
            
            # Parse response
            response_body = json.loads(response.get('body').read())
            
            # Debug print
            print("Raw response:", response_body)
            
            # Extract the generated text based on Mistral's response format
            if 'messages' in response_body:
                return response_body['messages'][0]['content'].strip()
            elif 'choices' in response_body:
                return response_body['choices'][0]['message']['content'].strip()
            else:
                print(f"Unexpected response format: {response_body}")
                return None
            
        except Exception as e:
            print(f"Error in analyze_transcript: {str(e)}")
            return None

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
                    result = self.analyze_transcript(self._read_transcript(filename))
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