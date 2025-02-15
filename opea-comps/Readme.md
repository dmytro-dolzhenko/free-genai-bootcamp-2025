# OPEA Mega and Microservices

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

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Ensure Docker and Docker Compose are installed on your machine.

## Quick Start

### Running LLM locally using Ollama

1. Start Ollama server using Docker Compose:
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
List of available models: [Ollama Library](https://ollama.com/library)

*Note: deepseek-r1:1.5b model has been chosen taking into account limited computational resources of the host machine.*

### Generate Text
Generate text using a specific model:
```bash
curl http://localhost:8008/api/generate -d '{
  "model": "deepseek-r1:1.5b",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

### List Local Models
List all models available on the local machine:
```bash
curl http://localhost:8008/api/tags
```

## Running Mega-Service (OPEA architecture)

### Start Mega-Service

1. Create a virtual environment and install dependencies:
    ```bash
    cd mega-service
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. Start the service:
    ```bash
    python app.py
    ```

### Chat Question Endpoint
Chat Question endpoint can be used in the following way:
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"messages": "Why the sky is blue?"}' http://localhost:8000/v1/chat/completions
```

## Usage

- Ensure Docker and Docker Compose are running.
- Use the provided API endpoints to interact with the AI models.

