from fastapi import FastAPI
from pydantic import BaseModel
from graph import agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):

    result = agent.invoke({
        "messages": [
            ("user", req.message)
        ]
    })

    return result