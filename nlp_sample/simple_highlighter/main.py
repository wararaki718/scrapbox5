from typing import List

from highlighter import Highlighter
from position import Position


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


def main():
    keywords = ["こんにちわ", "プログラマ", "す。", "プロク゛", "。"]
    text = "こんにちわ、ほ゛くはプロク゛ラマです。"

    highlighter = Highlighter()
    positions = highlighter.highlight(keywords, text)
    show(text, positions)

    print("DONE")


if __name__ == "__main__":
    main()
