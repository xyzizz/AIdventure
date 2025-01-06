import os
from pprint import pprint
from langchain_openai import AzureChatOpenAI
from src.latest_ai_development.configs import load_config, config
from langchain_core.messages import AIMessage

class LLMs:
    def build_azure_llm(self):
        azure_llm = AzureChatOpenAI(
            deployment_name=config.deployment_name,
            model=config.model,
            api_key=config.azure_api_key,
            api_version=config.azure_openai_api_ver,
            azure_endpoint=config.azure_api_base,
            temperature=0,
            max_retries=2,
        )
        return azure_llm

def test_azure():
    azure_llm = LLMs().build_azure_llm()

    messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
    ]
    ai_msg: AIMessage = azure_llm.invoke(messages)
    print(ai_msg.pretty_repr())


