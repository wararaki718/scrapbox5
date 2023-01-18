from .multiply import calc_multiply as mul_func


class Calculator:
    def __init__(self):
        pass

    def calc(self, a: int, b: int) -> int:
        return mul_func(a, b)
