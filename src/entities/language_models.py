from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

from src.settings import OPENAI_API_KEY, OPENAI_MODELS


class LangModels:
    def __init__(self, model_name: str = OPENAI_MODELS.get("gpt4-turbo")):
        self._llm = OpenAI(
            temperature=0, openai_api_key=OPENAI_API_KEY, model_name=model_name
        )
        self._chat = ChatOpenAI(api_key=OPENAI_API_KEY)

    @property
    def llm(self):
        return self._llm

    @property
    def chat(self):
        return self._chat
