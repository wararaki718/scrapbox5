from typing import Union

from app.add import Adder
from app.sub import Subtractor
from app.mul import Multiplier


class CalculatorFactory:
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, calc_type: str) -> Union[Adder, Subtractor, Multiplier]:
        if calc_type == "add":
            return Adder()
        
        if calc_type == "sub":
            return Subtractor()
        
        return Multiplier()
