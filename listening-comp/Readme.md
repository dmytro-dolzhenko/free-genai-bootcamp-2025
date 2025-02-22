# JLPT Practice Application

An AI-powered Japanese Language Proficiency Test (JLPT) practice application that generates interactive listening comprehension questions. The system uses AWS Bedrock and ChromaDB to create realistic JLPT-style questions with audio generation capabilities.

## Features

- 🎧 AI-generated JLPT listening practice questions
- 🗣️ Text-to-speech audio generation for questions
- 📝 Four JLPT listening test sections:
  - Task-based Comprehension
  - Quick Response
  - Short Conversations
  - Information/Monologue
- 🔍 Topic-based question organization
- 💡 Instant feedback and explanations
- 🔄 Dynamic question generation

## System Requirements

- Python 3.8+
- AWS Account with Bedrock access
- ChromaDB
- Streamlit
- ffmpeg (for audio processing)

## Dependencies

```bash
streamlit
boto3
chromadb
pydub
youtube_transcript_api
typing-extensions
```

## AWS Services Used

- AWS Bedrock
  - Mistral (mistral.mistral-large-2402-v1:0) for question generation
- AWS Polly
  - Text-to-speech service for generating audio files of conversations and monologues
  - Supports multiple Japanese voices for natural conversations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jlpt-practice.git
cd jlpt-practice
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up AWS credentials:
```bash
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=eu-west-1
```

4. Install ffmpeg (required for audio processing):

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
- Download from https://www.gyan.dev/ffmpeg/builds/
- Add to system PATH

## Usage

Run the Streamlit application:
```bash
streamlit run frontend/app.py
```

## Application Structure

### Frontend (Streamlit)
- Interactive web interface
- Category selection
- Four practice sections
- Audio playback
- Answer checking
- Dynamic question generation

### Backend
- ChromaDB for pattern storage
- AWS Bedrock integration
- Audio generation system
- Question analysis and generation

## Data Structure

### Question Format

```json
{
  "conversation": [
    {"speaker": "田中先生 (Tanaka Sensei)", "text": "Japanese text"},
    {"speaker": "田中太郎 (Tanaka Taro)", "text": "Japanese text"}
  ],
  "question_text": "Question in Japanese",
  "answer_options": ["Option 1", "Option 2", "Option 3", "Option 4"],
  "correct_answer": "Correct option",
  "explanation": "Explanation in English",
  "audio_path": "path/to/audio/file"
}
```

### Monologue Format

```json
{
  "monologue": {
    "speaker": "田中先生 (Tanaka Sensei)",
    "text": "Japanese announcement or explanation"
  },
  "question_text": "Question about the announcement",
  "answer_options": ["Option 1", "Option 2", "Option 3", "Option 4"],
  "correct_answer": "Correct option",
  "explanation": "Explanation in English",
  "audio_path": "path/to/audio/file"
}
```

## Configuration

Create a `config.yaml` in the project root:

```yaml
aws:
  region: eu-west-1
  model_id: mistral.mistral-large-2402-v1:0
chroma:
  persist_directory: chroma_db
```

## Troubleshooting

### Common Issues

1. AWS Bedrock Access
```
Error: botocore.exceptions.ClientError
Solution: Verify AWS credentials and Bedrock access
```

2. Audio Generation
```
Error: ffmpeg not found
Solution: Install ffmpeg and verify it's in system PATH
```

3. ChromaDB
```
Error: Failed to initialize ChromaDB
Solution: Check persistence directory permissions
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Roadmap

- [ ] Support for additional JLPT levels (N4-N1)
- [ ] User progress tracking
- [ ] More varied question patterns
- [ ] Enhanced audio generation quality
- [ ] Multiple voice options for conversations
- [ ] Practice session history

## Support

For support, please open an issue in the GitHub repository.

## Acknowledgments

- AWS Bedrock team
- ChromaDB team
- Streamlit team

