import os
from app.factory import CalculatorFactory


calc_type = os.getenv("CALC_TYPE", "add")
calculator = CalculatorFactory.create(calc_type)


def calc(a: int, b: int) -> int:
    return calculator.calc(a, b)


def main():
    a = 2
    b = 1
    result = calc(a, b)
    print(result)
    print("DONE")


if __name__ == "__main__":
    main()
