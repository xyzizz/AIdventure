# from tests.test_azure import test_azure
# from tests.test_crew import test_crew
# from tests.test_v_llm import test_vllm
import sys
from dotenv import load_dotenv
from src.latest_ai_development.main import run as run_summarize_crew
from src.alg.main import run as run_alg_crew
from src.news.main import run as run_news_crew

load_dotenv()


if __name__ == "__main__":
    run_news_crew()
