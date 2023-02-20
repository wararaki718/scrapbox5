from typing import List

from pydantic import BaseModel

from .news import News


class SearchResults(BaseModel):
    results: List[News]
