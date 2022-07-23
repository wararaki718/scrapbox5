from pydantic import BaseModel


class Result(BaseModel):
    value: int
