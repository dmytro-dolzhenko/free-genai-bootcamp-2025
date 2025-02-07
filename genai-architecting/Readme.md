# Generative AI Architecture

## Functional Overview

Proposed architecture leverages AWS Cloud services, Serverless approach, specifically, to implement a Retrieval-Augmented Generation (RAG) pipeline with guardrails for responsible AI usage. It integrates document storage, embeddings generation, vector database retrieval, and inference using Anthropic Claude Sonnet 3.5.

The system ensures structured input validation, controlled responses, and efficient document-based knowledge retrieval.

## Workflow

1. **Document Upload & Processing**
   - Users upload documents to an **S3 Knowledge Base**.
   - An **AWS Lambda** function is triggered upon upload.
   - The Lambda function generates **embeddings** using **AWS Bedrock** and stores them in **Pinecone Vector DB**.

2. **Prompt Processing & Response Generation**
   - The user submits a **prompt** via an **API Gateway**.
   - The API Gateway forwards the request to a **backend AWS Lambda** function.
   - Prompt is augmented using **RAG** (Retrieval-Augmented Generation) by querying **Pinecone Vector DB** for relevant embeddings.

3. **LLM Interaction & Guardrails**
   - The retrieved context and prompt are validated against **Input GuardRails**.
   - The validated input is sent to **Anthropic Claude Sonnet 3.5** (70B, max 200k tokens) via **AWS Bedrock**.
   - The generated response undergoes **Output GuardRails** for further validation.
   - The final response is sent back to the user.

## Key Considerations

- **Scalability:** The architecture is designed to handle large-scale document ingestion and prompt processing efficiently.
- **Security & Compliance:** By incorporating guardrails, we ensure responsible AI interactions and adherence to compliance standards.
- **Performance:** The use of **AWS Bedrock** and **Pinecone Vector DB** enables fast and relevant retrievals.
- **Flexibility:** The system can be extended to support additional AI models or enhanced retrieval strategies.

