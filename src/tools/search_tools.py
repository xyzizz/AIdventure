import base64
from typing import Type, Union
from crewai.tools import tool
from src.llm import VLLMs
from crewai import LLM
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from langchain_community.tools import DuckDuckGoSearchRun


class SearchInput(BaseModel):
    """Input schema for SearchTool."""

    query: Union[str, dict] = Field(..., description="The search query as a string or dictionary.")


class SearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = (
        "A wrapper around DuckDuckGo Search. "
    )
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        # query = "搜索最近24小时内最热门的10条科技新闻, 有关AI和区块链的新闻优先"
        res = DuckDuckGoSearchRun().run(query)
        return res
