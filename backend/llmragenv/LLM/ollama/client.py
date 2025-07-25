import re
from typing import List, overload
from llama_index.llms.ollama import Ollama
from overrides import override
from llama_index.core.utils import print_text

from llmragenv.LLM.llm_base import LLMBase
from logger import Logger


class OllamaClient(LLMBase):

    def __init__(self, model_name, url, key):
        super().__init__()
        self.model_name = model_name
        base_url = re.sub(r"/v\d+", "", url)
        print(base_url)

        self.client = Ollama(model=model_name, request_timeout=200, base_url=base_url)

        # self.logger = Logger("AIClient")
        # self.logger.info("Use llama_index backend to generate")
        print("Use llama_index backend to generate")

        response = self.chat_with_ai("who are you?")
        print_text(
            f"\n test llm model {self.model_name} : {response}\n", color="yellow"
        )

    @override
    def chat_with_ai(
        self, prompt: str, history: List[List[str]] | None = None
    ) -> str | None:

        response = self.client.complete(prompt)

        return response.text

    @override
    def chat_with_ai_stream(self, prompt: str, history: List[List[str]] | None = None):

        return self.client.stream_complete(prompt)
