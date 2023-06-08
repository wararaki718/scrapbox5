from functools import partial
from typing import List

from sudachipy import dictionary
from sudachipy.tokenizer import Tokenizer


class TextAnalyzer:
    def __init__(self) -> None:
        tokenizer = dictionary.Dictionary().create()
        self._tokenizer = partial(tokenizer.tokenize, mode=Tokenizer.SplitMode.C)

    def analyze(self, text: str) -> List[str]:
        tokens = []
        for token in self._tokenizer(text):
            if token.part_of_speech()[0] == "名詞":
                tokens.append(token.surface())
        return tokens
