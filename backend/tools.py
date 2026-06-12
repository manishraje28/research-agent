import os

from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults

load_dotenv()

search = TavilySearchResults(
    max_results=5,
    tavily_api_key=os.getenv("TAVILY_API_KEY"),
)

tools = [search]