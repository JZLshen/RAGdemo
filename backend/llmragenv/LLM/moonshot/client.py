from llmragenv.LLM.openai.client import OpenAIClient


class MoonshotClient(OpenAIClient):
    """
    Moonshot AI Client
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
