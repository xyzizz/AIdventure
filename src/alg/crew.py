import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from chromadb.utils.embedding_functions.openai_embedding_function import (
    OpenAIEmbeddingFunction,
)
from crewai_tools.tools.vision_tool.vision_tool import ImagePromptSchema

from src.alg.tool.custom_tool import AnalyseImageTool


from ..llm import LLMs


@CrewBase
class AlgorithmProblemProcesser:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def extractor(self) -> Agent:
        return Agent(
            config=self.agents_config["extractor"],
            llm=LLMs.default_llm(),
            verbose=True,
            tools=[AnalyseImageTool()],
            max_iter=1,
        )

    @agent
    def solver(self) -> Agent:
        return Agent(
            config=self.agents_config["solver"],
            llm=LLMs.default_llm(),
            verbose=True,
        )

    @task
    def extract_task(self) -> Task:
        return Task(
            config=self.tasks_config["extract_task"],
            agent=self.extractor(),
            output_file="outputs/extracted_data.txt",
            max_retries=0,
        )

    @task
    def solve_task(self) -> Task:
        return Task(
            config=self.tasks_config["solve_task"],
            agent=self.solver(),
            output_file="outputs/solve_task.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            # verbose=True,
        )
