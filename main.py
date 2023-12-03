# from src.app import start

# # start()

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import HumanMessage

from src.settings import OPENAI_API_KEY

chat_model = ChatOpenAI(api_key=OPENAI_API_KEY)
open_ai = OpenAI(api_key=OPENAI_API_KEY)

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

chat_model.invoke(messages)


def open_ai_invoke(prompt):
    try:
        response = open_ai(prompt)
    except Exception as e:
        print(e)
    return response


print(open_ai_invoke(text))
