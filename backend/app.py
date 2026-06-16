from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graph import agent
from memory import save_message, get_history
from prompts import RESEARCH_SYSTEM_PROMPT
 
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request Model
class ChatRequest(BaseModel):
    message: str


# Home Route
@app.get("/")
def home():
    return {
        "message": "PropResearch AI Running"
    }


# Chat Route
@app.post("/chat")
async def chat(req: ChatRequest):

    save_message("user", req.message)

    messages = [
        ("system", RESEARCH_SYSTEM_PROMPT),
        *get_history(),
    ]

    result = agent.invoke(
        {
            "messages": messages
        }
    )

    answer = result["messages"][-1].content

    save_message("assistant", answer)

    return {
        "response": answer
    }