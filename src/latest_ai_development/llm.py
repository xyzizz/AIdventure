import os
from crewai import LLM
from langchain_openai import AzureChatOpenAI, AzureOpenAI


class LLMs:
    @classmethod
    def default_llm(cls):
        default_llm = LLM(
            model = "openai/glm-4-flash",
            base_url="https://open.bigmodel.cn/api/paas/v4/",
            api_key=os.environ.get("ZHUPU_API_KEY")
        )
        return default_llm


    @classmethod
    def azure_llm(cls):
        azure_llm = AzureChatOpenAI(
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            model="gpt-4o",
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        return azure_llm

