from pydantic import BaseModel


class Result(BaseModel):
    score: float
