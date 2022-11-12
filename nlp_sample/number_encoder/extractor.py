from typing import List

from position import Position


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
        for i, c in enumerate(list(s+" ")):
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


if __name__ == "__main__":
    def show(text: str, positions: List[Position]):
        for position in positions:
            s = ""
            for i, c in enumerate(list(text)):
                if i == position.start:
                    s += "["
                
                s += c

                if i+1 == position.end:
                    s += "]"
            print(s, position)

    extractor = NumberExtractor()

    texts = [
        "二〇〇五年",
        "一二三四五六七八九",
        "千円",
        "これは二万七千円です。",
        "1億9千万人"
        "四千二百万",
        "10,000万円",
        "１億円",
        "FF10,10人月で開発しました。",
        "FF10,十人月で開発しました。",
        "10.6億円",
        "0.6人月",
        "110.110.110.110"
    ]
    for text in texts:
        positions = extractor.extract(text)
        show(text, positions)
