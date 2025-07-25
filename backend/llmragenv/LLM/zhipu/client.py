from llmragenv.LLM.openai.client import OpenAIClient


class ZhipuClient(OpenAIClient):
    """
    Zhipu AI Client
    """

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
