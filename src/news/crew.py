import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from chromadb.utils.embedding_functions.openai_embedding_function import (
    OpenAIEmbeddingFunction,
)
from crewai_tools.tools.vision_tool.vision_tool import ImagePromptSchema

from src.tools.search_tools import SearchTool


from ..llm import LLMs


@CrewBase
class NewsCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def retriever(self) -> Agent:
        return Agent(
            config=self.agents_config["retriever"],
            llm=LLMs.default(),
            verbose=True,
            tools=[SearchTool()],
        )

    @agent
    def translator(self) -> Agent:
        return Agent(
            config=self.agents_config["translator"],
            llm=LLMs.default(),
            verbose=True,
        )

    @agent
    def formatter(self) -> Agent:
        return Agent(
            config=self.agents_config["formatter"],
            llm=LLMs.default(),
            verbose=True,
        )

    @task
    def retrieve_task(self) -> Task:
        return Task(
            config=self.tasks_config["retrieve_task"],
            # output_file="outputs/news.md",
            max_retries=0,
            agent=self.retriever(),
        )

    @task
    def translate_task(self) -> Task:
        return Task(
            config=self.tasks_config["translate_task"],
            output_file="outputs/news.md",
            max_retries=0,
            agent=self.translator(),
        )

    @task
    def format_task(self) -> Task:
        return Task(
            config=self.tasks_config["format_task"],
            output_file="outputs/news.md",
            max_retries=0,
            agent=self.formatter(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            # verbose=True,
        )
