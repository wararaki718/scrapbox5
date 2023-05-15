from pydantic import BaseModel


class Request(BaseModel):
    a: int = 0
    b: int = 1
    mode: str = "add"


class Response(BaseModel):
    result: int
