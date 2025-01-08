import base64
from crewai.tools import tool
from src.llm import VLLMs
from crewai import LLM


@tool("Analyse Image")
def analyse_image(image_path: str) -> str:
    """Analyse an image containing an algorithm problem and return the text."""

    llm: LLM = VLLMs.default_llm()
    with open(image_path, "rb") as img_file:
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
    res = llm.call(messages)
    return res
