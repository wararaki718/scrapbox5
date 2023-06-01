from typing import Generator


def ngrams(text: str, size: int, sentinel: str = "_") -> Generator[str, None, None]:
    padding = sentinel * (size - 1)
    text = padding + text

    end = len(text) - size + 1
    for i in range(end):
        yield text[i:i+size]
