import os
from dotenv import load_dotenv

load_dotenv()

print("Groq:", os.getenv("GROQ_API_KEY"))
print("Tavily:", os.getenv("TAVILY_API_KEY"))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL_NAME = "llama-3.3-70b-versatile"