from functools import partial

from sudachipy import tokenizer, dictionary, MorphemeList


class TextAnalyzer:
    def __init__(self):
        mode = tokenizer.Tokenizer.SplitMode.C
        default_tokenizer = dictionary.Dictionary().create()
        self._tokenize = partial(default_tokenizer.tokenize, mode=mode)

    def analyze(self, text: str) -> MorphemeList:
        morphemes: MorphemeList = self._tokenize(text=text)
        return morphemes
