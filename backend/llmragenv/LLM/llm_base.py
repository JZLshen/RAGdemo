import json
from typing import List, Dict, Tuple

from openai import OpenAI, Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from utils.singleton import Singleton
from abc import abstractmethod


class LLMBase(metaclass=Singleton):
    """
    LLMBase is a generic LLM client that can be used to interact with any language model. But if you want to
    specify the model name, you can extend ClientBase.
    """

    def __init__(self):
        pass

    @abstractmethod
    def chat_with_ai(
        self, prompt: str, history: List[List[str]] | None = None
    ) -> str | None:
        raise NotImplementedError()

    @abstractmethod
    def chat_with_ai_stream(self, prompt: str, history: List[List[str]] | None = None):
        raise NotImplementedError()
