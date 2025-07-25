from llmragenv.LLM.openai.client import OpenAIClient


class DeepseekClient(OpenAIClient):
    """
    Deepseek AI Client
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
