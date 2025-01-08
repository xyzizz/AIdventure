from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from chromadb.utils.embedding_functions.openai_embedding_function import (
    OpenAIEmbeddingFunction,
)

from .tool.custom_tool import analyse_image

from ..llm import LLMs, VLLMs


@CrewBase
class AlgorithmProblemProcesser:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def extractor(self) -> Agent:
        return Agent(
            role="extractor",
            goal="Extract text from an image containing an algorithm problem",
            backstory="The agent is trained to extract text from images containing algorithm problems",
            # llm=VLLMs.default_llm(),
            verbose=True,
            tools=[analyse_image()],
        )
    
    @agent
    def solver(self) -> Agent:
        return Agent(
            role="solver",
            goal="Solve algorithm problems",
            backstory="The agent is trained to solve algorithm problems",
            llm=LLMs.default_llm(),
            verbose=True,
        )
    
    @task
    def extract_task(self) -> Task:
        return Task(
            config=self.tasks_config["extract_task"],
            agent=self.extractor(),
        )
    
    @task
    def solve_task(self) -> Task:
        return Task(
            config=self.tasks_config["solve_task"],
            agent=self.solver(),
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
    

def main():
    AlgorithmProblemProcesser().crew().kickoff()


if __name__ == "__main__":
    main()