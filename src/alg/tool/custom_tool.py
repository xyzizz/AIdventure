import base64
from crewai_tools import tool
from llm import VLLMs
from crewai import LLM


@tool("Analyse Image")
def analyse_image(img_path: str = "tests/image.png") -> str:

    llm: LLM = VLLMs.default_llm()
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
