from langchain_community.tools import TavilySearchResults

search = TavilySearchResults(
    max_results=5
)

tools = [
    search
]