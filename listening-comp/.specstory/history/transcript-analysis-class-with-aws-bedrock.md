## SpecStory

## Transcript Analysis Class with AWS Bedrock (2/21/2025, 10:04:10 PM)

_**User**_

@backend 
Please create a separate class within backend folder which will use AWS Bedrock to analyse every transcript file to extract key information from it - subject, different sections with clear questions and answers. section 3 which relies on pictures should be skipped.

---

_**Assistant**_

I'll help create a class to analyze the transcripts using AWS Bedrock. First, let's create a new file called `transcript_analyzer.py` in the backend folder.

```python:backend/transcript_analyzer.py
import boto3
import json
import os
from typing import Dict, List, Optional

class TranscriptAnalyzer:
    def __init__(self, transcript_dir: str = "transcripts"):
        """
        Initialize TranscriptAnalyzer with AWS Bedrock client and transcript directory.
        
        Args:
            transcript_dir (str): Directory containing transcript files
        """
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name='us-east-1'  # Update with your preferred region
        )
        self.transcript_dir = transcript_dir
        self.model_id = "anthropic.claude-v2"  # Using Claude V2 model
        
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
        Invoke AWS Bedrock with given prompt.
        
        Args:
            prompt (str): Prompt for the model
            
        Returns:
            str: Model's response
        """
        body = json.dumps({
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 4096,
            "temperature": 0,
            "top_p": 1
        })
        
        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            body=body
        )
        
        response_body = json.loads(response.get('body').read())
        return response_body.get('completion', '')

    def analyze_transcript(self, filename: str) -> Dict:
        """
        Analyze a transcript file to extract key information.
        
        Args:
            filename (str): Name of transcript file
            
        Returns:
            Dict: Analyzed information including subject, sections, and Q&A
        """
        transcript = self._read_transcript(filename)
        
        analysis_prompt = f"""
        Analyze this Japanese language test transcript and extract the following information:
        1. Subject/Level (e.g., JLPT N5)
        2. For each section (except section 3 with pictures), extract:
           - Section name/number
           - Type of questions
           - Each question and its context
           - Correct answers if provided
        
        Format the response as JSON with these keys:
        - subject: string
        - sections: list of section objects containing:
          - name: string
          - question_type: string
          - questions: list of objects containing:
            - question: string
            - context: string
            - correct_answer: string (if provided)
        
        Transcript:
        {transcript}
        """
        
        response = self._invoke_bedrock(analysis_prompt)
        
        try:
            # Clean up the response to ensure it's valid JSON
            json_str = response.strip()
            if json_str.startswith("```json"):
                json_str = json_str[7:-3]  # Remove ```json and ``` markers
            return json.loads(json_str)
        except json.JSONDecodeError:
            return {
                "error": "Failed to parse analysis response",
                "raw_response": response
            }

    def analyze_all_transcripts(self) -> Dict[str, Dict]:
        """
        Analyze all transcript files in the transcript directory.
        
        Returns:
            Dict[str, Dict]: Dictionary mapping filename to analysis results
        """
        results = {}
        for filename in os.listdir(self.transcript_dir):
            if filename.endswith('.txt'):
                try:
                    results[filename] = self.analyze_transcript(filename)
                except Exception as e:
                    results[filename] = {
                        "error": f"Failed to analyze transcript: {str(e)}"
                    }
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
```

This class provides the following functionality:

1. Initializes AWS Bedrock client for text analysis
2. Reads transcript files from the specified directory
3. Analyzes transcripts using Claude V2 model to extract:
   - Subject/Level information
   - Section details (excluding section 3 with pictures)
   - Questions and answers from each section
4. Saves analysis results in JSON format

To use this class, you'll need:

1. AWS credentials configured with access to Bedrock
2. The boto3 library installed

You can use it like this:

```python
# Example usage
analyzer = TranscriptAnalyzer()

# Analyze a single transcript
results = analyzer.analyze_transcript("0e0duD8_LFE.txt")

# Analyze all transcripts
all_results = analyzer.analyze_all_transcripts()

# Save results to file
analyzer.save_analysis(all_results)
```

Make sure to add these requirements to your `requirements.txt`:

```text:backend/requirements.txt
boto3>=1.28.0
youtube_transcript_api>=0.6.1
```

The analyzer will structure the information in a way that makes it easy to:
- Identify the test level and subject
- Extract questions and their context
- Skip the image-based section 3
- Preserve any provided answers

The JSON output will be well-structured and can be used for further processing or display in a UI.

---

_**User**_

@transcript_analyzer.py - update TranscripAnalyzer to pass region and model during class creation

---

_**Assistant**_

I'll modify the TranscriptAnalyzer class to accept region and model parameters during initialization.

```python:backend/transcript_analyzer.py
import boto3
import json
import os
from typing import Dict, List, Optional

class TranscriptAnalyzer:
    def __init__(self, 
                 transcript_dir: str = "transcripts",
                 region_name: str = "us-east-1",
                 model_id: str = "anthropic.claude-v2"):
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
        
    # ... rest of the class implementation remains the same ...
```

This change allows users to:
1. Specify a different AWS region if needed
2. Use a different Bedrock model if desired
3. Keep the default values for backward compatibility

You can now use the class in different ways:

```python
# Using defaults (us-east-1 region and Claude v2)
analyzer = TranscriptAnalyzer()

# Specifying a different region
analyzer = TranscriptAnalyzer(region_name="us-west-2")

# Specifying both region and model
analyzer = TranscriptAnalyzer(
    region_name="eu-west-1",
    model_id="anthropic.claude-instant-v1"
)
```

The rest of the class functionality remains unchanged, but now it's more flexible for different deployment scenarios.

---

_**User**_

what is the best way to supply AWS access key?

---

_**Assistant**_

The best practice for handling AWS credentials is to avoid hardcoding them in the code. Here are the recommended approaches in order of preference:

1. **Environment Variables** (Most recommended for development):
```python:backend/transcript_analyzer.py
import os
import boto3
import json
from typing import Dict, List, Optional

class TranscriptAnalyzer:
    def __init__(self, 
                 transcript_dir: str = "transcripts",
                 region_name: str = "us-east-1",
                 model_id: str = "anthropic.claude-v2",
                 aws_access_key_id: Optional[str] = None,
                 aws_secret_access_key: Optional[str] = None):
        """
        Initialize TranscriptAnalyzer with AWS Bedrock client and transcript directory.
        
        Args:
            transcript_dir (str): Directory containing transcript files
            region_name (str): AWS region name for Bedrock
            model_id (str): Bedrock model ID to use for analysis
            aws_access_key_id (Optional[str]): AWS access key ID
            aws_secret_access_key (Optional[str]): AWS secret access key
        """
        # If credentials provided, use them. Otherwise, boto3 will check environment variables
        credentials = {}
        if aws_access_key_id and aws_secret_access_key:
            credentials.update({
                'aws_access_key_id': aws_access_key_id,
                'aws_secret_access_key': aws_secret_access_key
            })
            
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name,
            **credentials
        )
        self.transcript_dir = transcript_dir
        self.model_id = model_id
```

You can use it in several ways:

1. Using environment variables (recommended):
```bash
# Set in your environment or .env file
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
```

```python
# The class will automatically use environment variables
analyzer = TranscriptAnalyzer()
```

2. Passing credentials directly (less secure, only for testing):
```python
analyzer = TranscriptAnalyzer(
    aws_access_key_id="your_access_key",
    aws_secret_access_key="your_secret_key"
)
```

3. **AWS IAM Role** (Best for production on AWS):
If running on AWS services (EC2, Lambda, etc.), use IAM roles and don't specify credentials at all. The AWS SDK will automatically use the instance's role.

4. **AWS Credentials File** (Good for local development):
Store credentials in `~/.aws/credentials`:
```ini
[default]
aws_access_key_id = your_access_key
aws_secret_access_key = your_secret_key
```

For your application, I recommend:
1. Development: Use environment variables with a `.env` file
2. Production: Use IAM roles if deploying to AWS
3. CI/CD: Use environment secrets in your CI/CD platform

You can create a `.env.example` file to show the required environment variables:

```text:backend/.env.example
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1
```

And add `.env` to your `.gitignore` to prevent accidentally committing credentials:

```text:.gitignore
.env
```

This approach provides flexibility while maintaining security best practices.

---

_**User**_

how .env will be picked up?

---

_**Assistant**_

We need to add python-dotenv to load the environment variables from the .env file. Let me help you set that up:

1. First, let's update requirements.txt:

```python:backend/requirements.txt
boto3>=1.28.0
youtube_transcript_api>=0.6.1
python-dotenv>=0.19.0
```

2. Then modify the TranscriptAnalyzer to load the .env file:

```python:backend/transcript_analyzer.py
import boto3
import json
import os
from typing import Dict, List, Optional
from dotenv import load_dotenv

class TranscriptAnalyzer:
    def __init__(self, 
                 transcript_dir: str = "transcripts",
                 region_name: str = None,
                 model_id: str = "anthropic.claude-v2",
                 aws_access_key_id: Optional[str] = None,
                 aws_secret_access_key: Optional[str] = None):
        """
        Initialize TranscriptAnalyzer with AWS Bedrock client and transcript directory.
        
        Args:
            transcript_dir (str): Directory containing transcript files
            region_name (str): AWS region name for Bedrock
            model_id (str): Bedrock model ID to use for analysis
            aws_access_key_id (Optional[str]): AWS access key ID
            aws_secret_access_key (Optional[str]): AWS secret access key
        """
        # Load environment variables from .env file
        load_dotenv()
        
        # Get credentials from parameters or environment variables
        credentials = {}
        if aws_access_key_id and aws_secret_access_key:
            credentials.update({
                'aws_access_key_id': aws_access_key_id,
                'aws_secret_access_key': aws_secret_access_key
            })
            
        # Get region from parameter or environment variable
        region_name = region_name or os.getenv('AWS_REGION', 'us-east-1')
            
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region_name,
            **credentials
        )
        self.transcript_dir = transcript_dir
        self.model_id = model_id
```

Now you can use the analyzer in these ways:

1. Using .env file:
```bash
# .env file
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1
```

```python
# Will automatically load credentials from .env
analyzer = TranscriptAnalyzer()
```

2. Using environment variables:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1
```

```python
# Will use environment variables
analyzer = TranscriptAnalyzer()
```

3. Passing credentials directly:
```python
analyzer = TranscriptAnalyzer(
    aws_access_key_id="your_key",
    aws_secret_access_key="your_secret",
    region_name="us-west-2"
)
```

The load_dotenv() function will:
1. Look for a .env file in the current directory
2. Load any variables defined there into the environment
3. Not override existing environment variables

This provides a convenient way to manage configuration in development while still supporting other deployment scenarios.

---



---

