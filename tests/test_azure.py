from crewai import LLM
from dotenv import load_dotenv
from llm import LLMs
from langchain_core.messages import AIMessage

load_dotenv()


def test_azure():
    azure_llm: LLM = LLMs.azure()

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that translates English to French. Translate the user sentence.",
        },
        {
            "role": "user",
            "content": "I love programming.",
        },
    ]

    print(azure_llm.call(messages))


if __name__ == "__main__":
    test_azure()
