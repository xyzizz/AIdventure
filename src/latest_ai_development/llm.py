import os
from crewai import LLM
from langchain_openai import AzureChatOpenAI, AzureOpenAI


class LLMs:
    @classmethod
    def default_llm(cls) -> LLM:
        return cls.zhupu_llm()

    @classmethod
    def zhupu_llm(cls) -> LLM:
        zhupu_llm = LLM(
            model=os.getenv("ZHUPU_MODEL", "openai/glm-4-flash"),
            base_url=os.getenv("ZHUPU_API_ENDPOINT"),
            api_key=os.getenv("ZHUPU_API_KEY"),
        )
        return zhupu_llm

    @classmethod
    def azure_llm(cls) -> LLM:
        azure_llm = LLM(
            model=os.getenv("AZURE_MODEL"),
            base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
        )
        return azure_llm
