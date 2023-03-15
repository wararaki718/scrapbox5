from functools import partial
from typing import List

from sudachipy import tokenizer, dictionary


class TextAnalyzer:
    def __init__(self):
        mode = tokenizer.Tokenizer.SplitMode.C
        default_tokenizer = dictionary.Dictionary().create()
        self._tokenize = partial(default_tokenizer.tokenize, mode=mode)

    def analyze(self, text: str) -> List[str]:
        return [morph.surface() for morph in self._tokenize(text=text)]
