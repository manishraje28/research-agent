from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from memory import save_message, get_history
from graph import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Research Agent Running"
    }


@app.post("/chat")
async def chat(req: ChatRequest):

    save_message("user", req.message)

    result = agent.invoke(
        {
            "messages": get_history()
        }
    )

    answer = result["messages"][-1].content

    save_message("assistant", answer)

