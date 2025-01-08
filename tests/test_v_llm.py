import base64
from dotenv import load_dotenv
from llm import VLLMs
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


def test_vllm_local():
    llm: LLM = VLLMs.default_llm()
    img_path = "tests/image.png"
    with open(img_path, "rb") as img_file:
        img_base = base64.b64encode(img_file.read()).decode("utf-8")
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": img_base}},
                {"type": "text", "text": "解析图片里的这道算法题，以文字格式返回"},
            ],
        }
    ]
    print(llm.call(messages))

def test_vllm():
    # test_vllm_url()
    test_vllm_local()

if __name__ == "__main__":
    test_vllm()
