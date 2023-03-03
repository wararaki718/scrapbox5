from pydantic import BaseModel


class Result(BaseModel):
    survived: int
