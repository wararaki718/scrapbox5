from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Request(BaseModel):
    name: str = ""
    age: int = 0
    location: Optional[str] = None
    keyword: Optional[str] = "test"


class Response(BaseModel):
    message: str


@app.get("/ping")
def ping() -> str:
    return "pong"


@app.post("/greeting", response_model=Response)
def greeting(request: Request) -> Response:
    message = f"{request.name}: {request.age}: {request.location}: {request.keyword}"
    return Response(message=message)
