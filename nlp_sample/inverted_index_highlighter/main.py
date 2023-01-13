from typing import List

from highlighter import Highlighter
from schema import Position


def show(text: str, positions: List[Position]):
    for position in positions:
        s = ""
        for i, c in enumerate(text):
            if i == position.start:
                s += "["
            
            s += c

            if i+1 == position.end:
                s += "]"
        print(s)


def main():
    keywords = ["こんにちわ", "プログラマ", "す。", "プロク゛", "。", "ク゛ク゛", "desu.", "゛", "10", "F1", "20", "500", "200000"]
    text = "こんにちわ、ほ゛くはプロク゛ラマです。プロク゛ク゛ク゛ク゛ラマdesu.FFX.パソコンを二十万円で買いました。電源は５００ワットです。"

    highlighter = Highlighter()
    positions = highlighter.highlight(keywords, text)
    show(text, positions)

    print("DONE")


if __name__ == "__main__":
    main()
