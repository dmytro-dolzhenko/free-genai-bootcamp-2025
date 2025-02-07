# Japanese Sentence Constructor

Difficulty: Level 100

## Business Goal: 
A chat agent that acts as a teaching assistant to guide students from translating a target English sentence into Japanese. The teaching assistant is not there to provide the direct answer, only guidance.

## Models 

Number of models with different context size, number of parameters, hosting options have been utilised and evaluated. They are summarised in the table below.

### Model Comparison Table

| Model Name                         |Parameters| Max Tokens | Hosting                   | Pricing               | Accuracy & Performance | Japanese Language Support | Notes |
|------------------------------------|----------|-----------|---------------------------|-----------------------|------------------------|---------------------------|---------------------------|
| **ChatGPT-4o**                     |1.8T      | 128k      | OpenAI (Cloud-based)      | Free plan available   | Best                   | Excellent                 | Strong general reasoning, coding, and multilingual support. |
| **Mistral Large (24.02)**          |32B       | 32k       | AWS Bedrock (Ireland)     | AWS pricing applies   | Acceptable             | Moderate                  | Suitable for complex tasks. Japanese support is decent but not as strong as GPT-4o. |
| **DeepSeek R1 Distill Llama 8B**   |8B        | 4k / 8k   | Local (LM Studio)         | Free (self-hosted)    | Very Limited           | Limited                   | Requires GPU for smooth performance. Japanese support is weaker. |
| **Titan Text G1 - Express**        |7B        | 8k        | AWS Bedrock (Ireland)     | AWS pricing applies   | Unusable / Crashed     | Limited                   | Optimized for efficiency. May struggle with Japanese. |




### ChatGPT-4o (Best Performance)
**Why It Performed Best:**
- **Multilingual Excellence**: Strong **Japanese support**, outperforming others in fluency and contextual understanding.  
- **High Accuracy & Reasoning**: Best for **complex tasks, problem-solving, and coding** with deep contextual retention.  
- **Optimized for Performance**: **Low latency, highly efficient,** and cloud-hosted on OpenAI’s infrastructure.  
- **Large Context Window**: Handles **128k tokens**, enabling better long-form coherence and memory retention.  
- **Versatile Applications**: Excels in **technical, creative, and conversational AI tasks** across multiple domains.  

**Weaknesses:**
- **Cloud-based only** (no self-hosting like DeepSeek R1 Distill).  
- **OpenAI’s pricing model applies** for API access.  

---

### Mistral Large (24.02)
**Why It Performed Well (But Not as Good as ChatGPT-4o):**
- **High Token Limit (32k)**: Better than **Titan G1** but lower than **GPT-4o’s 128k**.  
- **Decent Japanese Support**: Not as strong as **GPT-4o** but better than **DeepSeek R1 and Titan**.  
- **AWS Bedrock Hosting**: Reliable but depends on **AWS pricing and infrastructure constraints**.  
- **Well-Optimized for Complex Tasks**: Good balance of **performance and cost efficiency**.  

**Weaknesses:**
- **Moderate Japanese support**, struggles with complex structures.  
- **Less refined for general reasoning** compared to GPT-4o.  
- **Dependent on AWS Bedrock**, limiting customization options.  

---

### DeepSeek R1 Distill Llama 8B
**Why It Performed Moderately Well:**
- **Runs Locally**: No cloud costs; fully **self-hosted using LM Studio**.  
- **Optimized for Performance**: Well-tuned for **efficiency in local AI setups**.  
- **Decent Accuracy in English Tasks**: Can handle **structured text processing** well.  

**Weaknesses:**
- **Weak Japanese Language Support**: Struggles with **grammar, fluency, and tokenization in Japanese**.  
- **Limited Context Window**: Cannot match **Mistral or GPT-4o** in long-form responses.  
- **Requires High-Performance Hardware**: Needs **GPU for fast processing**.  

---

### Titan Text G1 - Express (Worst Performance)
**Why It Performed the Worst:**
- **Optimized for Efficiency**: Works well in **low-compute environments**.  
- **AWS Bedrock Hosted**: Integrates well into **AWS ecosystems**.  

**Weaknesses:**
- **Weakest Japanese Support**: Struggles with **complex sentence structures and meaning retention**.  
- **Lowest Context Window (8k)**: Handles **significantly fewer tokens** than GPT-4o or Mistral Large.  
- **Moderate Accuracy & Reasoning**: Less effective in **complex tasks** than other models.  





