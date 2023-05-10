from .calculator import Calculator
from .schema.config import CalculatorConfig


def main():
    config = CalculatorConfig(mode="sub")
    calculator = Calculator(config)
    
    x = 3
    y = 2
    result = calculator.compute(x, y)
    print(f"{x} - {y} = {result}")
    print("DONE")
