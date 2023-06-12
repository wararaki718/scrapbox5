from enum import Enum, IntEnum

from pydantic import BaseModel


class AnimalEnum(str, Enum):
    cat = "cat"
    dog = "dog"


class AgeEnum(IntEnum):
    one = 1
    two = 2


class User(BaseModel):
    name: str
    animal: AnimalEnum
    age: AgeEnum
