from dotenv import load_dotenv
from src.latest_ai_development.llm import LLMs
from langchain_core.messages import AIMessage

load_dotenv()

def test_azure():
    azure_llm = LLMs.azure_llm()

    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg: AIMessage = azure_llm.invoke(messages)
    print(ai_msg.pretty_repr())