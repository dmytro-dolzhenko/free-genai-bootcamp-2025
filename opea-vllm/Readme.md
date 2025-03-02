# OPEA vLLM Project with Megaservice utilising Qwen2.5 Model

## Overview

This project provides a complete end-to-end solution for deploying and interacting with the Qwen2.5-0.5B-Instruct language model using OPEA Megaservice and vLLM for efficient inference. The project comprises three main components:

1. **vLLM Docker Image**: A containerized environment that runs the Qwen/Qwen2.5-0.5B-Instruct model from Hugging Face using vLLM for optimized inference.
2. **OPEA Megaservice**: A gateway service that handles API requests and communicates with the vLLM service.
3. **UI Application**: A simple Streamlit-based web interface that allows users to interact with the model through the Megaservice.

## Project Structure

```
vllm/
├── build_docker_vllm.sh       # Script to build the vLLM Docker image
├── docker-compose.yaml        # Docker Compose configuration for all services
├── launch_vllm_service.sh     # Script to launch the vLLM service independently
├── .gitignore                 # Git ignore file
├── megaservice/               # Megaservice component
│   ├── Dockerfile             # Dockerfile for the Megaservice
│   ├── megaservice.py         # Main Megaservice implementation
│   └── requirements.txt       # Python dependencies for the Megaservice
└── ui/                        # UI component
    ├── Dockerfile             # Dockerfile for the UI application
    ├── app.py                 # Streamlit application code
    └── requirements.txt       # Python dependencies for the UI
```

## Prerequisites

- Docker and Docker Compose
- Windows Subsystem for Linux (WSL) if running on Windows
- Git
- Internet connection to download models and dependencies
- Hugging Face account and token (for accessing the model)

## Setup and Installation

### 1. Configure WSL (for Windows users)

If you're using Windows, properly configure WSL to avoid build issues:

1. Open PowerShell or Command Prompt as Administrator
2. Run the following command to open the WSL config file:
   ```powershell
   notepad $env:USERPROFILE\.wslconfig
   ```
3. Add or modify the following settings:
   ```ini
   [wsl2]
   memory=8GB    # Increase if you have more RAM
   processors=4  # Adjust based on your CPU
   swap=8GB      # Helps prevent out-of-memory crashes
   ```
4. Save the file and restart WSL:
   ```powershell
   wsl --shutdown
   ```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd opea-vllm
```

### 3. Set Environment Variables

Create a `.env` file in the project root with your Hugging Face token:

```bash
echo "HF_TOKEN=your_hugging_face_token" > .env
```

Replace `your_hugging_face_token` with your actual Hugging Face token.

### 4. Build the vLLM Docker Image

Follow the instructions from the [vLLM README](https://github.com/opea-project/GenAIComps/blob/main/comps/third_parties/vllm/README.md) to build the vLLM Docker image with CPU hardware mode.

Use the provided script to build the vLLM Docker image:

```bash
chmod +x build_docker_vllm.sh
./build_docker_vllm.sh
```

This script will:
- Clone the vLLM repository
- Checkout the latest stable version
- Build a Docker image with the necessary dependencies

If the build fails or crashes your system, try limiting parallel compilation jobs:

```bash
export MAX_JOBS=2
./build_docker_vllm.sh
```

## Running the Project

### Using Docker Compose (Recommended)

The easiest way to run the entire project is using Docker Compose:

```bash
docker-compose up
```

This will start all three components:
- vLLM server on port 80 (internal)
- Megaservice on port 8888 (internal)
- UI application on port 8501 (exposed to the outside world)

### Running vLLM Service Independently

If you want to run just the vLLM service:

```bash
chmod +x launch_vllm_service.sh
./launch_vllm_service.sh 8009 Qwen/Qwen2.5-0.5B-Instruct cpu
```

Parameters:
- Port number 
- Model name 
- Hardware mode (default: cpu, alternative: hpu)
- Parallel number (for HPU mode)

## Accessing the Application

Once all services are running:

1. Review vLLM service logs within Docker Container to ensure that it's fully loaded Qwen/Qwen2.5-0.5B-Instruct model and ready to accept requests. Usually it takes around 10 minutes based on utilised hardware.
   
   Look for following message in the logs:
   ```text
   INFO:     Started server process [1]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```

2. Open a web browser
3. Navigate to http://localhost:8501
4. Enter your prompt in the text field
5. Click "Submit" to get a response from the model

## Troubleshooting

### Build Failures

If the Docker build fails:

1. Ensure WSL has enough resources (see WSL configuration above)
2. Limit parallel jobs with `export MAX_JOBS=2`
3. Check Docker has enough memory allocated
4. Ensure you have a valid Hugging Face token

### Connection Issues

If services can't communicate:

1. Check that all containers are running: `docker ps`
2. Verify network configuration in docker-compose.yaml
3. Check logs for specific errors: `docker logs <container-name>`

### Model Download Issues

If the model fails to download:

1. Verify your Hugging Face token is valid
2. Check internet connectivity
3. Ensure the model name is correct

## Advanced Configuration

The project can be customized through environment variables in the docker-compose.yaml file:

- `LLM_MODEL_ID`: Change the model being used
- `VLLM_SKIP_WARMUP`: Control model warmup behavior
- `VLLM_TORCH_PROFILER_DIR`: Directory for profiling data
- `MEGASERVICE_HOST_IP` and `MEGASERVICE_PORT`: Configure Megaservice networking
- `LLM_HOST_IP` and `LLM_ENDPOINT_PORT`: Configure vLLM service networking
