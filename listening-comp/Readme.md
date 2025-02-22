# JLPT Practice Application

A comprehensive application for practicing Japanese Language Proficiency Test (JLPT) questions, powered by AI and vector search technology. The system analyzes Japanese language lesson videos, extracts practice questions, and generates new questions following similar patterns.

## Features

- 🎯 Automated transcription of Japanese language lesson videos
- 🔍 AI-powered analysis of lesson content and question patterns
- 📝 Generation of JLPT-style practice questions
- 🗄️ Vector-based storage and retrieval of questions
- 🌐 Interactive web interface for practice sessions

## System Architecture

The application consists of three main components:

### Backend

- `YouTubeTranscriber`: Handles video transcription
- `TranscriptAnalyzer`: Analyzes transcripts using AWS Bedrock (Mistral)
- `VectorStoreLoader`: Manages the ChromaDB vector database

### Frontend

- Streamlit-based web interface
- Interactive question practice interface
- Category-based navigation
- Real-time question generation

### Database

- ChromaDB for vector storage
- Stores questions, patterns, and metadata
- Enables semantic search for similar questions

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

3. Set up AWS credentials for Bedrock:

```bash
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

## Usage

### 1. Transcribe Videos

```python
from backend.youtube_transcriber import YouTubeTranscriber
transcriber = YouTubeTranscriber()
transcriber.transcribe("https://www.youtube.com/watch?v=video_id", "ja")
```

### 2. Analyze Transcripts

```python
from backend.transcript_analyzer import TranscriptAnalyzer
analyzer = TranscriptAnalyzer(
region_name="eu-west-1",
model_id="mistral.mistral-large-2402-v1:0"
)
results = analyzer.analyze_transcript("transcript_file.txt")
```

### 3. Load Vector Store

```python
from backend.vector_store_loader import VectorStoreLoader
loader = VectorStoreLoader(persist_directory="chroma_db")
collection = loader.load_vectorized_data(
vectorized_data_path="vectorized_data",
collection_name="japanese_lessons"
)
```

### 4. Run Web Interface

```bash
streamlit run frontend/app.py
```

## Data Structure

### Transcript Analysis Output

```json
{
"video_id": "video_id",
"topic": "JLPT N5 Listening Test",
"introduction": {
"greeting": "...",
"lesson_overview": "...",
"target_audience": "..."
},
"questions": [
{
"question_text": "...",
"context": "...",
"answer_options": ["..."],
"correct_answer": "..."
}
]
}
```


### Vector Store Documents

- Question documents
- Pattern documents
- Metadata documents

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Requirements

- Python 3.8+
- AWS Account with Bedrock access
- ChromaDB
- Streamlit
- YouTube Data API credentials
- ffmpeg (required for audio processing)

## Configuration

Create a `config.yaml` file in the project root:


```yaml
aws:
region: eu-west-1
model_id: mistral.mistral-large-2402-v1:0
chroma:
persist_directory: chroma_db
frontend:
title: JLPT Practice Questions
theme: light
```

## Troubleshooting

### Common Issues

1. AWS Credentials
```bash
Error: botocore.exceptions.ClientError: An error occurred (UnrecognizedClientException)
Solution: Check AWS credentials are properly set
```

2. ChromaDB
```bash
Error: Failed to load vector store
Solution: Ensure ChromaDB is properly installed and running
```
3. Video Transcription
```bash
Error: youtube_dl.utils.DownloadError
Solution: Update youtube-dl or check video URL validity
```

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- AWS Bedrock team for the Mistral model
- ChromaDB team for the vector database
- YouTube Data API team

## Roadmap

- [ ] Add support for other JLPT levels
- [ ] Implement user authentication
- [ ] Add progress tracking
- [ ] Expand question patterns
- [ ] Improve question generation quality

## Installing ffmpeg

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows
1. Download ffmpeg from https://www.gyan.dev/ffmpeg/builds/
2. Download "ffmpeg-release-essentials.zip"
3. Extract to a location (e.g., C:\ffmpeg)
4. Add the bin folder (C:\ffmpeg\bin) to your system's PATH:
   - Open System Properties > Advanced > Environment Variables
   - Under System Variables, find and select "Path"
   - Click Edit > New
   - Add the path to ffmpeg bin folder (e.g., C:\ffmpeg\bin)
   - Click OK on all windows
5. Restart your terminal/IDE

### macOS
```bash
brew install ffmpeg
```

Verify installation by running:
```bash
ffmpeg -version
```

