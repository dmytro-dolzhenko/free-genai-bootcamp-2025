from comps import register_microservice, EmbedDoc, ServiceRoleType, ServiceType, TextDoc
from comps import MicroService, ServiceOrchestrator
import requests

class MegaService:
    def __init__(self, host="localhost", port=8000):    
        self.host = host
        self.port = port
        self.megaservice = ServiceOrchestrator()
        self.endpoint = "/v1/chat/question"

    def add_remote_service(self, service_ip, service_port):        
        llm = MicroService(
            name="opea_service@text_generation_ollama",
            host=service_ip,
            port=service_port,
            endpoint="/v1/generate",
            service_type=ServiceType.LLM,
            use_remote_service=True,
            input_datatype=TextDoc,
            output_datatype=TextDoc
        )
        self.megaservice.add(llm)

    async def handle_request(self, request: dict) -> TextDoc:
        response_message = f"Received: {request}"
        print(response_message)

        try:
            print(self.megaservice.services)
            result_dict, runtime_graph = await self.megaservice.schedule(
                initial_inputs={"text": request['messages']},
                service_name="opea_service@text_generation_ollama",
            )

            print(f"response result: {result_dict}")

        except Exception as e:
            print(f"Error: {e}")

        return TextDoc(text=response_message)

    def start(self):

        self.service = MicroService(
            self.__class__.__name__,
            service_role=ServiceRoleType.MEGASERVICE,
            host=self.host,
            port=self.port,
            endpoint=self.endpoint,
            input_datatype=dict,
            output_datatype=TextDoc,
        )

        self.service.add_route(self.endpoint, self.handle_request, methods=["POST"])
        self.service.start()

       

OLLAMA_API_URL = "http://localhost:8008/api/generate"

@register_microservice(
    name="opea_service@text_generation_ollama",
    service_type=ServiceType.LLM,
    endpoint="/v1/generate",
    host="0.0.0.0",
    port=6000,
    input_datatype=TextDoc,
    output_datatype=TextDoc,
)
def generate_text(input: TextDoc) -> TextDoc:
    print(f"generate_text called with input: {input}")

    try:
        payload = {
            "model": "deepseek-r1:1.5b",  
            "prompt": input.text,  
            "stream": False
        }
        print (f'ollama request {input}')
        response = requests.post(OLLAMA_API_URL, json=payload)
        response_data = response.json()
        print (f'ollama response {response_data}')
        generated_text = response_data["response"]
        return TextDoc(text=generated_text)
    except Exception as e:
        print(f"Error in generate_text: {e}")
        return TextDoc(text=f"Error: {e}")

mega_service = MegaService()
mega_service.add_remote_service("localhost", 6000)    
mega_service.start()