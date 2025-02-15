## SpecStory

## Creating README.md for AI Model API Project (2/15/2025, 4:22:26 PM)

_**User**_

Could you please write Readme.md for me which will summarise a content of the project, docker-compose, OPEA

---

_**Assistant**_

I'll help you create a comprehensive README.md file that explains the project, its setup, and usage.

```markdown:Readme.md
# AI Model API Server

This project provides a REST API server for running AI language models locally using Docker containers.

## Overview

The service allows you to:
- Run AI models locally through a REST API
- Support for multiple model backends (including deepseek-r1)
- OpenAI-compatible API endpoints

## Prerequisites

- Docker
- Docker Compose
- At least 8GB RAM (16GB recommended)
- NVIDIA GPU (optional, but recommended for better performance)

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Start the services using Docker Compose:
```bash
docker-compose up -d
```

## API Endpoints

### Pull Model
Pull a specific model to use with the service:

```bash
curl http://localhost:8008/api/pull -d '{
  "model": "deepseek-r1:1.5b"
}'
```

### Chat Completions
The API is compatible with OpenAI's chat completion endpoint. You can use it in two ways:

1. Simple text query:
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -d "Why the sky is blue?"
```

2. JSON format (recommended):
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Why the sky is blue?"
      }
    ]
  }'
```

## Configuration

The service can be configured through environment variables in the `docker-compose.yml` file:

```yaml
services:
  api:
    environment:
      - MODEL_PATH=/path/to/models
      - MAX_TOKENS=2048
      - ...
```

## Models

Currently supported models:
- deepseek-r1:1.5b
- (list other supported models)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]
```

This README provides a basic structure that you can further customize based on your specific project details. You may want to add:

1. More detailed configuration options
2. Complete list of supported models
3. Troubleshooting section
4. System requirements
5. Performance considerations
6. Security notes
7. Development setup instructions

Would you like me to expand on any of these sections?

---



---

