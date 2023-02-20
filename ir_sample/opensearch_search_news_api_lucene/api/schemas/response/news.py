from pydantic import BaseModel


class News(BaseModel):
    docid: str
    newsid: str
    context: str
