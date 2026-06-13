from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from tools import tools
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY
)

agent = create_react_agent(
    llm,
    tools
)