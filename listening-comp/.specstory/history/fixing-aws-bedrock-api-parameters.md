## SpecStory

## Fixing AWS Bedrock API Parameters (2/21/2025, 10:11:07 PM)

_**User**_

@transcript_analyzer.py 



---

_**Assistant**_

I see the error - it's related to the Bedrock API parameters. The error indicates that `max_tokens_to_sample` is not a valid parameter for the model. Let me help you fix the `_invoke_bedrock` method in the TranscriptAnalyzer class.

```python:backend/transcript_analyzer.py
    def _invoke_bedrock(self, prompt: str) -> str:
        """
        Invoke AWS Bedrock with given prompt.
        
        Args:
            prompt (str): Prompt for the model
            
        Returns:
            str: Model's response
        """
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 4096,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0,
            "top_p": 1
        })
        
        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            body=body
        )
        
        response_body = json.loads(response.get('body').read())
        return response_body.get('content', '')
```

The changes made:
1. Updated the request body format to match Claude's API requirements in Bedrock
2. Changed `max_tokens_to_sample` to `max_tokens`
3. Restructured the prompt to use the messages format
4. Updated the response parsing to get 'content' instead of 'completion'

This should resolve the validation error you're seeing. The error occurred because the API parameters were not matching the expected format for Claude models in AWS Bedrock.

---

_**User**_

Can we use Converse API and what's the difference?

---

_**Assistant**_

Yes, you can use the Claude Conversation (Converse) API through AWS Bedrock. The main difference is in how you structure conversations and maintain context. Here's a comparison:

1. Messages API (current implementation):
- Newer API format
- Cleaner way to handle multi-turn conversations
- More explicit role definitions (user/assistant)
- Better suited for chat-like interactions
- What we're currently using with `"messages": [{"role": "user", "content": prompt}]`

2. Converse API (alternative):
- Legacy/original API format
- Uses a single string with "Human: " and "Assistant: " prefixes
- Requires manual formatting of conversation history
- More suited for simple one-shot completions
- Would look like this:

```python:backend/transcript_analyzer.py
    def _invoke_bedrock(self, prompt: str) -> str:
        """
        Invoke AWS Bedrock with given prompt using Converse API.
        """
        body = json.dumps({
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens": 4096,
            "temperature": 0,
            "top_p": 1,
            "anthropic_version": "bedrock-2023-05-31"
        })
        
        response = self.bedrock.invoke_model(
            modelId=self.model_id,
            body=body
        )
        
        response_body = json.loads(response.get('body').read())
        return response_body.get('completion', '')
```

For your current use case (analyzing transcripts), either API would work fine since you're doing single-turn interactions. However, I recommend sticking with the Messages API (current implementation) because:
1. It's the more modern approach
2. It's more maintainable if you need to add multi-turn conversations later
3. It's more explicit about the roles in the conversation
4. It's the recommended format for newer Claude models

---



---

