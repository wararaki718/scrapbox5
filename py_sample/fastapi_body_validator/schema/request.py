from pydantic import BaseModel, Field


class Params(BaseModel):
    a: int
    b: int
    mode: str = Field(default="add", description="calculation type", max_length=5)
