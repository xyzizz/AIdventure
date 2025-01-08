import base64
from dotenv import load_dotenv
from src.llm import VLLMs
from crewai import LLM

load_dotenv()


def test_vllm_url():
    llm: LLM = VLLMs.default_llm()

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "图里有什么"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://img1.baidu.com/it/u=1369931113,3388870256&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1703696400&t=f3028c7a1dca43a080aeb8239f09cc2f"
                    },
                },
            ],
        }
    ]

    print(llm.call(messages))


def test_vllm():
    test_vllm_url()


if __name__ == "__main__":
    test_vllm()
