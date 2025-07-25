from llmragenv.LLM.openai.client import OpenAIClient


class QwenClient(OpenAIClient):
    """
    Qwen AI Client
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
