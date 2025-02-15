## SpecStory

## Routing Requests to Ollama Text Generation (2/15/2025, 2:30:29 PM)

_**User**_

How to make sure that handle_request routes request to opea_service@text_generation_ollama

---

_**Assistant**_

I'll help you modify the `handle_request` method to properly route requests to the Ollama text generation service. The main issue is that we need to properly connect the services and format the input correctly.

Here's the necessary edit:

```python:app.py
async def handle_request(self, request: dict) -> TextDoc:
    # ... existing code ...

    # Convert the messages into a single prompt string
    messages = request['messages']
    prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    await self.megaservice.schedule(
        initial_inputs={"text": prompt},
        service_name="opea_service@text_generation_ollama"  # Specify the target service
    )

    # Get the result from the service orchestrator
    result = await self.megaservice.get_result()
    return TextDoc(text=result['text'])
```

The key changes are:
1. Converting the chat messages into a format that the Ollama service can understand (a single text prompt)
2. Specifying the target service name in the `schedule` call
3. Waiting for and returning the actual result from the service orchestrator

Also, make sure that the service is properly registered when you add it to the MegaService. You might want to update the `add_remote_service` method to register the service with the orchestrator:

```python:app.py
def add_remote_service(self, service_ip, service_port):        
    llm = MicroService(
        name="opea_service@text_generation_ollama",  # Match the registered service name
        host=service_ip,
        port=service_port,
        endpoint=self.endpoint,
        use_remote_service=True,
        service_type=ServiceType.LLM,
    )
    self.megaservice.register_service(llm)  # Register the service with the orchestrator
```

These changes will ensure that requests are properly routed to your Ollama text generation service.

---

_**User**_

I can see any requests comming to my ollama service

---

_**Assistant**_

Let's debug this by modifying the code to properly format the input and add some logging to track the request flow. Here's the suggested edit:

```python:app.py
async def handle_request(self, request: dict) -> TextDoc:
    response_message = f"Received: {request}"
    print(response_message)

    try:
        # Format messages into a single text string that Ollama can understand
        messages = request['messages']
        prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
        print(f"Formatted prompt: {prompt}")  # Debug log

        result_dict, runtime_graph = await self.megaservice.schedule(
            initial_inputs={"text": prompt},  # Send formatted text instead of raw messages
            service_name="opea_service@text_generation_ollama"
        )

        print(f"response result: {result_dict}")
        return TextDoc(text=result_dict.get('text', 'No response'))

    except Exception as e:
        print(f"Error: {e}")
        return TextDoc(text=str(e))
```

The main issue was that we were passing the raw messages array to the service, but the `generate_text` function expects a `TextDoc` with a text string. The changes:

1. Format the messages into a single text string
2. Pass the formatted text in the `initial_inputs`
3. Added more logging to help track the request flow
4. Improved error handling and response formatting

Also, make sure your `generate_text` function is properly registered by checking that:
1. The service name matches exactly ("opea_service@text_generation_ollama")
2. The port (6000) is correct and available
3. The service is actually running and accessible

You can add a test print statement in your `generate_text` function to verify it's being called:

```python:app.py
@register_microservice(
    name="opea_service@text_generation_ollama",
    service_type=ServiceType.LLM,
    endpoint="/v1/generate",
    host="localhost",
    port=6000,
    input_datatype=TextDoc,
    output_datatype=TextDoc,
)
def generate_text(input: TextDoc) -> TextDoc:
    print(f"generate_text called with input: {input}")  # Debug log
    payload = {
        "model": "deepseek-r1:1.5b",  
        "prompt": input.text,  
        "stream": False
    }
    # ... rest of the function
```

---

_**User**_

how is it used?

---

_**Assistant**_

The endpoint in the `@register_microservice` decorator specifies the URL path where this service will be exposed. Let's check if there's a mismatch between the endpoints.

Looking at your code, I notice that there might be an endpoint mismatch:

```python:app.py
# In MegaService.__init__
self.endpoint = "/v1/chat/completions"  # This is used for the main service

# In the microservice registration
@register_microservice(
    name="opea_service@text_generation_ollama",
    # ... other params ...
    endpoint="/v1/generate",  # This is a different endpoint!
)
```

Let's make sure the endpoints match. You should either:

1. Update the microservice registration to match the chat completions endpoint:
```python:app.py
@register_microservice(
    name="opea_service@text_generation_ollama",
    service_type=ServiceType.LLM,
    endpoint="/v1/chat/completions",  # Match the endpoint used in MegaService
    host="localhost",
    port=6000,
    input_datatype=TextDoc,
    output_datatype=TextDoc,
)
```

OR

2. Update the MegaService to use the generate endpoint:
```python:app.py
def __init__(self, host="localhost", port=8000):    
    self.host = host
    self.port = port
    self.endpoint = "/v1/generate"  # Match the endpoint used in the microservice
    self.megaservice = ServiceOrchestrator()
```

The endpoint is used to:
1. Define where the service listens for requests
2. Route requests to the correct handler
3. Enable service discovery and communication between services

Make sure all services that need to communicate are using matching endpoints.

---

_**User**_

curl -X POST "http://localhost:6000/v1/generate" -H "Content-Type: application/json" -d '{"text": "Hello"}' call is just hanging. However, I can see a listener on port 6000

---

_**Assistant**_

This suggests that while the service is running and listening on port 6000, it might not be properly handling the incoming requests. Let's debug the microservice registration and handling.

Here's how we can modify the code to add more debugging and ensure proper request handling:

```python:app.py
@register_microservice(
    name="opea_service@text_generation_ollama",
    service_type=ServiceType.LLM,
    endpoint="/v1/generate",
    host="localhost",
    port=6000,
    input_datatype=TextDoc,
    output_datatype=TextDoc,
)
async def generate_text(input: TextDoc) -> TextDoc:  # Make the function async
    print(f"generate_text called with input: {input}")
    try:
        payload = {
            "model": "deepseek-r1:1.5b",  
            "prompt": input.text,  
            "stream": False
        }
        print(f'Sending request to Ollama: {payload}')
        response = requests.post(OLLAMA_API_URL, json=payload)
        response_data = response.json()
        print(f'Ollama response: {response_data}')
        generated_text = response_data["response"]
        return TextDoc(text=generated_text)
    except Exception as e:
        print(f"Error in generate_text: {e}")
        raise
```

The key changes are:
1. Made the `generate_text` function `async` since it's being called in an async context
2. Added more error handling and logging
3. Made sure the function properly returns a `TextDoc`

Also, let's verify that the service is properly started. At the bottom of your file:

```python:app.py
if __name__ == "__main__":
    import asyncio
    
    print("Starting MegaService...")
    mega_service = MegaService()
    print("Adding remote service...")
    mega_service.add_remote_service("localhost", 6000)    
    print("Starting service...")
    mega_service.start()
    
    # Keep the main thread running
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
```

Try running the service again with these changes and see if the curl request works. The logs should help identify where the request is getting stuck.

Also, you can test if the Ollama service itself is responding correctly with:

```bash
curl -X POST "http://localhost:8008/api/generate" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek-r1:1.5b", "prompt": "Hello", "stream": false}'
```

This will help determine if the issue is with your service or with the Ollama backend.

---



---

