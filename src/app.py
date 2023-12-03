from langchain.schema import HumanMessage

from src.entities.language_models import LangModels


def start():
    text = input("Enter message: ")
    message = [HumanMessage(content=text)]
    # LangModels.llm.invoke(text)
    LangModels.chat.invoke(message)
