from calculator import Calculator
from extractor import NumberExtractor


class NumberConverter:
    def __init__(self):
        self._calculator = Calculator()
        self._extractor = NumberExtractor()

    def convert(self, s: str) -> str:
        positions = self._extractor.extract(s)
        for position in positions[::-1]:
            value = self._calculator.calculate(s[position.start:position.end])
            s = "".join((s[:position.start], value, s[position.end:]))
        return s
