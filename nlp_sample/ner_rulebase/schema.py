from typing import List

from pydantic import BaseModel
from sudachipy import MorphemeList


class Entity(BaseModel):
    name: str
    span: List[int]
    type: str


class NamedEntity(BaseModel):
    curid: str
    text: str
    entities: List[Entity]


class AnnotatedEntity(BaseModel):
    name: str
    span: List[int]
    type: str
    is_correct: bool


class AnnotatedNamedEntity(BaseModel):
    curid: str
    tokens: MorphemeList
    entities: List[AnnotatedEntity]

    class Config:
        arbitrary_types_allowed = True


class Result(BaseModel):
    index: int
    surface: str
    # span: List[int]
