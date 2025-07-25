from llmragenv.LLM.openai.client import OpenAIClient


class DoubaoClient(OpenAIClient):
    """
    豆包 AI Client
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
