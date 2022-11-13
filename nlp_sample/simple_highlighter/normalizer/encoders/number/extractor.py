from typing import List

from schema import Position


class NumberExtractor:
    def __init__(self):
        numbers = list("1234567890")
        full_numbers = list("１２３４５６７８９０")
        kanji_numbers = list("一二三四五六七八九〇壱弐参")
        digits = list("十百千")
        large_digits = list("万億兆")
        self._target = numbers + full_numbers + kanji_numbers + digits + large_digits

    def extract(self, s: str) -> List[Position]:
        positions = []
        index = None
        for i, c in enumerate(s+" "): # add offset
            if c in self._target:
                if index is None:
                    index = i
                continue

            # commma and dot check
            if 0 < i < len(s) and (c == "," or c == ".") and (s[i-1].isdigit() and s[i+1].isdigit()):
                continue

            if index is not None:
                positions.append(Position(start=index, end=i))
                index = None

        if index is not None:
            positions.append(Position(start=index,end=len(s)))

        return positions
