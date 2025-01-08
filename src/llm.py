import os
from crewai import LLM


class LLMs:
    @classmethod
    def default_llm(cls) -> LLM:
        return cls.zhipu_llm()

    @classmethod
    def zhipu_llm(cls) -> LLM:
        zhipu_llm = LLM(
            model=os.getenv("ZHIPU_MODEL"),
            base_url=os.getenv("ZHIPU_API_ENDPOINT"),
            api_key=os.getenv("ZHIPU_API_KEY"),
        )
        return zhipu_llm

    @classmethod
    def azure_llm(cls) -> LLM:
        azure_llm = LLM(
            model=os.getenv("AZURE_MODEL"),
            base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
        )
        return azure_llm


class VLLMs:
    @classmethod
    def default_llm(cls) -> LLM:
        return cls.zhipu_llm()

    @classmethod
    def zhipu_llm(cls) -> LLM:
        zhipu_llm = LLM(
            model=os.getenv("ZHIPU_V_MODEL"),
            base_url=os.getenv("ZHIPU_API_ENDPOINT"),
            api_key=os.getenv("ZHIPU_API_KEY"),
        )
        return zhipu_llm
