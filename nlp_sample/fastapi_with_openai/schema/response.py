from pydantic import BaseModel


class Reply(BaseModel):
    content: str
