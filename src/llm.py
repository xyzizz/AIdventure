import os
from crewai import LLM
from langchain_google_genai import ChatGoogleGenerativeAI


class LLMs:
    @classmethod
    def default(cls) -> LLM:
        return cls.zhipu()

    @classmethod
    def zhipu(cls) -> LLM:
        zhipu_llm = LLM(
            model=os.getenv("ZHIPU_MODEL", "openai/glm-4-flash"),
            base_url=os.getenv(
                "ZHIPU_API_ENDPOINT", "https://open.bigmodel.cn/api/paas/v4/"
            ),
            api_key=os.getenv("ZHIPU_API_KEY"),
        )
        return zhipu_llm

    @classmethod
    def zhipu_plus(cls) -> LLM:
        zhipu_llm = LLM(
            model=os.getenv("ZHIPU_MODEL_PLUS", "openai/glm-4-plus"),
            base_url=os.getenv("ZHIPU_API_ENDPOINT"),
            api_key=os.getenv("ZHIPU_API_KEY"),
        )
        return zhipu_llm

    @classmethod
    def azure(cls) -> LLM:
        azure_llm = LLM(
            model=os.getenv("AZURE_MODEL"),
            base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
        )
        return azure_llm

    @classmethod
    def deepseek(cls) -> LLM:
        deepseek_llm = LLM(
            model="openai/deepseek-chat",
            base_url="https://api.deepseek.com/v1/",
            api_key=os.getenv("DEEPSEEK_API_KEY"),
        )
        return deepseek_llm

    @classmethod
    def gemini(cls) -> LLM:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            verbose=True,
            temperature=0.5,
            goggle_api_key=os.getenv("GEMINI_API_KEY"),
        )
        return llm


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
