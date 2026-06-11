from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools import tools
from config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

agent = create_agent(
    llm,
    tools
)