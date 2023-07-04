from fastapi import FastAPI

from schema.config import PromptConfig
from schema.request import Message
from schema.response import Reply
from service import OpenAIService


app = FastAPI()

config = PromptConfig()
service = OpenAIService(**config.get_config())


@app.get("/ping")
def ping() -> str:
    return "pong\n"


@app.post("/chat", response_model=Reply)
def chat(message: Message) -> Reply:
    content = service.chat(message)
    return Reply(content=content)
