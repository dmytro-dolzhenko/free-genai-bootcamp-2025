## SpecStory

## Debugging Unreachable generate_text Function (2/15/2025, 2:30:29 PM)

_**User**_

Could you please figure out why generate_text is unreachable and how to fix it?

---

_**Assistant**_

Looking at your code, I can identify a few issues that might be causing `generate_text` to be unreachable. The main problem is a mismatch in the input types and how the messages are being passed. Here are the necessary changes:

1. In `handle_request`, you're passing a dictionary with 'messages' as text, but the `generate_text` function expects a `TextDoc` input.

2. The service registration for `generate_text` specifies `TextDoc` as input, but you're trying to pass a dictionary of messages directly.

Here's how to fix these issues:

```python:app.py
// ... existing code ...

async def handle_request(self, request: dict) -> TextDoc:
    response_message = f"Received: {request}"
    print(response_message)

    try:
        # Convert the messages to a format that generate_text can handle
        messages_text = "\n".join([msg.get('content', '') for msg in request['messages']])
        
        result_dict, runtime_graph = await self.megaservice.schedule(
            initial_inputs={"text": TextDoc(text=messages_text)},  # Wrap the text in TextDoc
            service_name="opea_service@text_generation_ollama"
        )

        print(f"response result: {result_dict}")
        return TextDoc(text=result_dict.get('text', 'No response'))

    except Exception as e:
        print(f"Error: {e}")
        return TextDoc(text=f"Error: {str(e)}")

// ... existing code ...

@register_microservice(
    name="opea_service@text_generation_ollama",
    service_type=ServiceType.LLM,
    endpoint="/v1/generate",
    host="0.0.0.0",
    port=6000,
    input_datatype=TextDoc,
    output_datatype=TextDoc,
)
async def generate_text(input: TextDoc) -> TextDoc:
    print(f"generate_text called with input: {input}")

    try:
        payload = {
            "model": "deepseek-r1:1.5b",  
            "prompt": input.text,  # Use the text field from TextDoc
            "stream": False
        }
        print(f'ollama request {input}')
        response = requests.post(OLLAMA_API_URL, json=payload)
        response_data = response.json()
        print(f'ollama response {response_data}')
        generated_text = response_data["response"]
        return TextDoc(text=generated_text)
    except Exception as e:
        print(f"Error in generate_text: {e}")
        return TextDoc(text=f"Error: {str(e)}")

// ... existing code ...
```

The key changes are:

1. In `handle_request`, we now:
   - Extract the message contents and join them into a single text
   - Wrap the text in a `TextDoc` object before passing it to `schedule`
   - Return the response properly

2. In `generate_text`, we:
   - Keep the input type as `TextDoc`
   - Access the text content using `input.text`
   - Ensure all error messages are properly converted to strings

These changes should make the service properly reachable and handle the message flow correctly. The main issue was that we weren't properly converting between the chat message format and the `TextDoc` format that the service expects.

Also, make sure that:
1. The Ollama service is running and accessible at `http://localhost:8008`
2. The deepseek model is available in your Ollama installation
3. The service is properly registered and running on port 6000

You might want to add more logging to track the flow of data through the system. If you're still having issues, please share any error messages you're seeing.

---

_**User**_

I think there is some problem with service registration. I can't curl it directly using port 6000

---

_**Assistant**_

Ah, I see the issue now. The problem is likely with how the service is being registered and started. The `generate_text` function is decorated with `@register_microservice`, but it needs to be properly initialized and started as a service. Let's modify the code to ensure the service starts correctly:

```python:app.py
// ... existing code ...

# Create a standalone service for the text generation
text_generation_service = MicroService(
    name="opea_service@text_generation_ollama",
    service_type=ServiceType.LLM,
    host="0.0.0.0",
    port=6000,
    endpoint="/v1/generate",
    input_datatype=TextDoc,
    output_datatype=TextDoc,
)

@register_microservice(
    name="opea_service@text_generation_ollama",
    service_type=ServiceType.LLM,
    endpoint="/v1/generate",
    host="0.0.0.0",
    port=6000,
    input_datatype=TextDoc,
    output_datatype=TextDoc,
)
async def generate_text(input: TextDoc) -> TextDoc:
    // ... existing generate_text code ...

# At the bottom of the file, replace the existing startup code with:
if __name__ == "__main__":
    # Start the text generation service
    text_generation_service.add_route("/v1/generate", generate_text, methods=["POST"])
    text_generation_service.start()

    # Start the mega service
    mega_service = MegaService()
    mega_service.add_remote_service("localhost", 6000)    
    mega_service.start()
```

The key changes are:

1. Creating an explicit `MicroService` instance for the text generation service
2. Adding the route to the service explicitly
3. Starting both services when the script runs

Now you should be able to:
1. Access the text generation service directly on port 6000
2. Access the mega service on port 8000

You can test the text generation service directly with curl:

```bash
curl -X POST http://localhost:6000/v1/generate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, how are you?"}'
```

Make sure you're running the script directly (not importing it) so that the `if __name__ == "__main__":` block executes. This will ensure both services start properly.

---

_**User**_

How do I tell it to invoke generate_text for processing?

---

_**Assistant**_

Looking at your code, I notice that the `generate_text` function is decorated with `@register_microservice` but isn't being invoked. Let's modify the code to properly invoke the service:

```python:app.py
// ... existing code ...

async def handle_request(self, request: dict) -> TextDoc:
    response_message = f"Received: {request}"
    print(response_message)

    try:
        # Get the last message content
        last_message = request['messages'][-1]['content']
        
        # Create TextDoc input
        input_doc = TextDoc(text=last_message)
        
        # Directly call generate_text
        response = await generate_text(input_doc)
        
        print(f"response result: {response}")
        return response

    except Exception as e:
        print(f"Error: {e}")
        return TextDoc(text=f"Error: {str(e)}")

// ... rest of the code ...
```

The key changes are:
1. Extract the last message content from the request
2. Create a TextDoc with that content
3. Directly call `generate_text` with the TextDoc input
4. Return the response from `generate_text`

This should now properly invoke the text generation function. The previous code was trying to use the scheduler but wasn't properly connecting to the generate_text function.

You can test this with a curl command like:

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello, how are you?"}]}'
```

---

_**User**_

I want to add @register_microservice to megaservice.add

---

_**Assistant**_



Ah, I understand now. You want to register the `generate_text` service with the MegaService during initialization. Let's modify the `add_remote_service` method to use the registered service:

```python:app.py
def add_remote_service(self, service_ip, service_port):        
    llm = MicroService(
        name="opea_service@text_generation_ollama",  # Match the name in @register_microservice
        host=service_ip,
        port=service_port,
        endpoint="/v1/generate",  # Match the endpoint in @register_microservice
        use_remote_service=True,
        service_type=ServiceType.LLM,
        input_datatype=TextDoc,  # Match the input type in @register_microservice
        output_datatype=TextDoc,  # Match the output type in @register_microservice
    )
    
    # Register the generate_text function with this service
    llm.add_route("/v1/generate", generate_text, methods=["POST"])
    
    self.megaservice.add(llm)
```

The key changes are:
1. Making sure all the service parameters match those in the `@register_microservice` decorator
2. Adding the `generate_text` function as a route to the service
3. Adding input and output datatypes to match the registration

This should now properly connect the registered `generate_text` function to the MegaService's routing system. When you make a request to the MegaService, it should be able to find and invoke the `generate_text` function through the scheduler.

The service registration will now be properly connected to both the direct endpoint (port 6000) and through the MegaService scheduler.

---



---

