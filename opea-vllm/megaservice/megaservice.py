import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('megaservice')

# Disable OpenTelemetry
os.environ['OTEL_SDK_DISABLED'] = "true"

from comps import ServiceOrchestrator, ServiceRoleType, MicroService, ServiceType
from comps.cores.proto.docarray import LLMParams
from comps.cores.proto.api_protocol import (
    ChatCompletionRequest, 
    ChatCompletionResponse
)
from comps.cores.mega.utils import handle_message
from fastapi import Request

class Chat:
    def __init__(self):
        logger.info('Initializing Chat service')
        self.megaservice = ServiceOrchestrator()
        self.endpoint = '/megaservice'
        self.host = os.getenv('MEGASERVICE_HOST_IP', '127.0.0.1')
        self.port = int(os.getenv('MEGASERVICE_PORT', '8888'))
    
    def add_remote_services(self):
        logger.info('Adding remote services')

        llm = MicroService(
            name="vLLM",
            host=os.getenv('LLM_HOST_IP', '127.0.0.1'),
            port=int(os.getenv('LLM_ENDPOINT_PORT', '8009')),
            endpoint="/v1/chat/completions",
            use_remote_service=True,
            service_type=ServiceType.LLM,
        )
        self.megaservice.add(llm)

        logger.info(f'Added service: {llm.name}')

   
    def start(self):
        logger.info('Starting service')
        self.service = MicroService(
            self.__class__.__name__,
            service_role=ServiceRoleType.MEGASERVICE,
            host=self.host,
            port=self.port,
            endpoint=self.endpoint,
            input_datatype=ChatCompletionRequest,
            output_datatype=ChatCompletionResponse
        )

        self.service.add_route(self.endpoint, self.handle_request, methods=["POST"])

        self.service.start()
    
    async def handle_request(self, request: Request):
        data = await request.json()
        logger.debug(f'Request data: {data}')
        
        chat_request = ChatCompletionRequest.model_validate(data)
        prompt = handle_message(chat_request.messages)

        logger.debug(f'Prompt: {prompt}')
        logger.debug(f'Chat request: {chat_request}')
        logger.debug(f'Chat request type: {chat_request.model_dump()}')

        # Get model from the request or use a default
        model = getattr(chat_request, 'model', 'Qwen/Qwen2.5-0.5B-Instruct')
        
        # Create a properly formatted request for vLLM
        vllm_request = {
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        
        logger.debug(f'vLLM request: {vllm_request}')

        llm_parameters = LLMParams(
            stream=False,
            model=model
        )

        logger.info(f'Sending request to vLLM with model: {model}')
        result_dict, runtime_graph = await self.megaservice.schedule(
            initial_inputs=vllm_request,
            llm_parameters=llm_parameters
        )

        response = result_dict["vLLM/MicroService"]["choices"][0]["message"]["content"]
        logger.info('Response received from vLLM')
        return response


if __name__ == '__main__':
    logger.info('Starting megaservice application')

    chat = Chat()
    chat.add_remote_services()
    chat.start()