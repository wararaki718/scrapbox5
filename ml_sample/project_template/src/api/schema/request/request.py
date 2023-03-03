from pydantic import BaseModel


class Passenger(BaseModel):
    Pclass: int
    Age: int
    Embarked: str
