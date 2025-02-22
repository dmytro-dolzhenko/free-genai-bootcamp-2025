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
- AWS Account with Bedrock and Polly access
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
  - Mistral (mistral.mistral-large-2402-v1:0) LLM for question generation
- AWS Polly
  - Text-to-speech service for generating audio files of conversations and monologues
  - Supports multiple Japanese voices for natural conversations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dmytro-dolzhenko/free-genai-bootcamp-2025.git
cd listening-comp
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
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

## Data Examples

### Transcript Examples

```json
{
  "transcripts": [
    {
      "id": "conv_001",
      "type": "conversation",
      "content": [
        {
          "speaker": "山田さん",
          "text": "すみません、図書館は何時まで開いていますか？",
          "translation": "Excuse me, until what time is the library open?"
        },
        {
          "speaker": "職員",
          "text": "平日は午後9時までです。土日は午後5時で閉まります。",
          "translation": "On weekdays it's open until 9 PM. On weekends it closes at 5 PM."
        }
      ],
      "topics": ["library", "schedule", "daily_life"],
      "difficulty": "N5"
    },
    {
      "id": "mono_001",
      "type": "monologue",
      "content": {
        "speaker": "アナウンサー",
        "text": "お知らせいたします。台風の影響により、本日の午後3時以降の電車の運行を見合わせる可能性がございます。",
        "translation": "Attention please. Due to the typhoon, train services may be suspended after 3 PM today."
      },
      "topics": ["announcement", "weather", "transportation"],
      "difficulty": "N4"
    }
  ]
}
```

These transcripts serve as the base content for generating listening comprehension questions. They include:
- Natural conversations and announcements in Japanese
- English translations for reference
- Topic tags for organization
- JLPT level indicators
- Speaker identification

### Vectorized Data Examples

```json
{
  "vectorized_patterns": [
    {
      "id": "pattern_001",
      "pattern_type": "quick_response",
      "embedding": [0.123, -0.456, 0.789, ...],
      "template": {
        "question_structure": "どうして{subject}は{action}のですか？",
        "context_requirements": ["reason", "explanation", "time_reference"],
        "difficulty_markers": ["casual_form", "て_form", "から_explanation"]
      }
    },
    {
      "id": "pattern_002",
      "pattern_type": "information_retrieval",
      "embedding": [-0.234, 0.567, -0.890, ...],
      "template": {
        "question_structure": "{event}の{aspect}について、正しいものはどれですか？",
        "context_requirements": ["event_details", "time", "location", "condition"],
        "difficulty_markers": ["passive_form", "formal_speech", "conditional_statements"]
      }
    }
  ]
}
```

The vectorized data is stored in ChromaDB and serves several purposes:
- Question pattern matching and retrieval
- Similarity search for generating related questions
- Template storage for dynamic question generation
- Difficulty level calibration
- Context requirements tracking

These patterns help ensure:
- Consistent question formatting
- Appropriate difficulty levels
- Natural language variations
- Context-appropriate questions
- Proper answer distribution

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
