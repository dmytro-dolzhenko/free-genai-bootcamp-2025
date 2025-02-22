# Japanese Writing Practice Application

An AI-powered Japanese handwriting practice application that generates random sentences and validates user handwriting using OCR technology. Built with Streamlit for an interactive web interface.

## Features

- 🎲 Random Japanese sentence generation using LLM (Ollama)
- ✍️ Handwriting input and validation
- 🔍 Real-time OCR comparison
- 📊 Detailed logging system
- 🌐 Interactive web interface with Streamlit

## System Requirements

- Python 3.8+
- Ollama running locally with Llama 3.2 3B model
- Streamlit
- Manga OCR

## AI Models

### LLM
- **Model**: Llama 3.2 3B via Ollama
- **Purpose**: Japanese sentence generation
- **Example Response**:
```json
{
    "japanese": "をこない",
    "english": "Someone will come."
}
```

### OCR
- **Model**: Manga OCR
- **Purpose**: Handwriting recognition and validation
- **Features**: Multi-orientation text detection

## Dependencies

```bash
streamlit
manga-ocr
requests
pillow
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dmytro-dolzhenko/free-genai-bootcamp-2025.git
cd writing-practice
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate 
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Ensure Ollama is running locally at http://localhost:8008

To start Ollama, run the following command:
```bash
cd opea-comps
docker-compose up -d
```

5. Ensure Python Flask backend is running:

To start the Python Flask backend, run the following command:
```bash
cd lang-portal/backend-flask
invoke init-db
python app.py
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Click "Generate Sentence" to get a new Japanese sentence
3. Write the sentence in the drawing area
4. Submit for validation

## Application Structure

### Frontend (Streamlit)
- Interactive web interface
- Drawing canvas
- Sentence generation controls
- Validation feedback

### Backend
- Ollama integration for sentence generation
- Manga OCR for handwriting recognition
- Comprehensive logging system

### Prompts
The `prompts/` directory contains YAML files that define the system prompts used for AI interactions:

```yaml
sentence_generation:
  template: |
    You are a Japanese language expert...
```

These templates ensure consistent and well-structured interactions with the LLM.

## Example Interaction

From the logs, here's a typical interaction flow:

```
2025-02-22 15:31:47,984 - INFO - Starting random sentence generation for group 1
2025-02-22 15:31:48,005 - INFO - Selected word: neru (to sleep)
2025-02-22 15:31:55,334 - INFO - Generated sentence: この夜に Sleep する
2025-02-22 15:31:55,336 - INFO - Successfully generated random sentence

2025-02-22 15:32:58,936 - INFO - Drawing submitted for comparison
2025-02-22 15:32:59,334 - DEBUG - Detected text in orientation: 円は昨年。
2025-02-22 15:32:59,725 - INFO - Best detected text: 円は昨年。 (similarity: 0.6)
2025-02-22 15:33:31,145 - INFO - Drawing did not match target text

2025-02-22 15:33:36,008 - INFO - Starting random sentence generation for group 1
2025-02-22 15:33:36,025 - INFO - Selected word: kuru (to come)
2025-02-22 15:33:43,689 - INFO - Generated sentence: をこない
2025-02-22 15:34:12,248 - INFO - Drawing submitted for comparison
2025-02-22 15:34:12,665 - DEBUG - Detected text in orientation: をこない
2025-02-22 15:34:13,021 - INFO - Best detected text: をこない (similarity: 1.0)
2025-02-22 15:34:38,218 - INFO - Drawing matched target text
```

## Logging

The application maintains detailed logs in the `logs/` directory:

### 1. Application Logs (`app_[date].log`)
General application flow and status:
```
2025-02-22 15:27:22,061 - INFO - Starting application
2025-02-22 15:27:22,061 - INFO - Connecting to Ollama at http://localhost:8008
2025-02-22 15:27:22,062 - INFO - Starting model initialization
2025-02-22 15:27:24,157 - INFO - Model verified and ready
2025-02-22 15:28:33,957 - INFO - Generate sentence button clicked
```

### 2. Drawing Comparison Logs (`drawing_comparison_[date].log`)
Detailed OCR comparison results:
```
2025-02-22 15:30:05,807 - INFO - Starting OCR comparison for target text: カるこない
2025-02-22 15:31:07,900 - DEBUG - Detected text in orientation: ヵろこない
2025-02-22 15:31:08,265 - DEBUG - Detected text in orientation: イベントは、
2025-02-22 15:31:08,266 - INFO - Best detected text: ヵろこない (similarity: 0.6)
```

### 3. Sentence Generator Logs (`sentence_generator_[date].log`)
LLM interaction and sentence generation details:
```
2025-02-22 15:33:36,008 - INFO - Starting random sentence generation for group 1
2025-02-22 15:33:36,009 - INFO - Fetching random word from group 1
2025-02-22 15:33:36,025 - INFO - Selected word: kuru (to come)
2025-02-22 15:33:36,026 - INFO - Generating sentence for word: kuru (to come)
2025-02-22 15:33:43,689 - DEBUG - Extracted JSON text: {"japanese": "\u3092\u3053\u306a\u3044", "english": "Someone will come."}
2025-02-22 15:33:43,690 - INFO - Successfully generated random sentence
```

## Project Structure

```
writing-practice/
├── app.py             # Main Streamlit application
├── prompts/           # LLM prompt templates
├── logs/              # Application logs
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

- [ ] Support for different JLPT levels
- [ ] User progress tracking
- [ ] Additional writing practice patterns
- [ ] Enhanced OCR accuracy
- [ ] Practice session history

## Support

For support, please open an issue in the GitHub repository.