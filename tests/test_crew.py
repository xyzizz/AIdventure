import os
from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
import litellm

from src.latest_ai_development.main import run


litellm.set_verbose = True

load_dotenv()


def test_crew():
    run()


if __name__ == "__main__":
    test_crew()
