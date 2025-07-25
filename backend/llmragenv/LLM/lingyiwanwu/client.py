from llmragenv.LLM.openai.client import OpenAIClient


class LingyiwanwuClient(OpenAIClient):
    """
    Ling yi wan wu AI Client
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
