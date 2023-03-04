from typing import List

from pydantic import BaseModel


class PreprocessedData(BaseModel):
    Pclass: List[List[int]]
    Age: List[List[int]]
    Embarked: List[List[str]]
    Ages: List[List[int]]
