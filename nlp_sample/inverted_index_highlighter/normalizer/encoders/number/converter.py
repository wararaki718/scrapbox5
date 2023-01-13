from typing import List

from .calculator import Calculator
from .extractor import NumberExtractor
from schema import Character, LinkType


class NumberConverter:
    def __init__(self):
        self._calculator = Calculator()
        self._extractor = NumberExtractor()

    def convert(self, tokens: List[Character]) -> List[Character]:
        s = "".join(map(str, tokens))
        positions = self._extractor.extract(s)
        for position in positions[::-1]:
            if (tokens[position.start].link == LinkType.NODE
                or tokens[position.start].link == LinkType.TAIL
                or tokens[position.end-1].link == LinkType.HEAD
                or tokens[position.end-1].link == LinkType.NODE):
                continue

            value = self._calculator.calculate(s[position.start:position.end])
            values = [Character(tokens[position.start].index, c, LinkType.NODE) for c in value]
            if len(values) == 1:
                values[0].link = LinkType.NONE
            else:
                values[0].link = LinkType.HEAD
                values[-1].link = LinkType.TAIL

            tokens = tokens[:position.start] + values + tokens[position.end:]
        return tokens
