import re
import unicodedata
from pathlib import Path
from typing import List, Tuple

from schema.lang import Lang
from schema.pair import Pair


def normalize(s: str) -> str:
    text = "".join(
        filter(
            lambda c: unicodedata.category(c) != "Mn",
            unicodedata.normalize("NFD", s)
        )
    )
    text = text.lower().strip()
    text = re.sub(r"([.!?])", r" \1", text)
    text = re.sub(r"[^a-zA-Z!?]+", r" ", text)
    return text.strip()


class LangReader:
    def __init__(self) -> None:
        pass

    def read(self, filename: Path, lang1: str, lang2: str, reverse: bool=False) -> Tuple[Lang, Lang, List[Pair]]:
        pairs: List[Pair] = []
        with open(filename) as f:
            for line in f:
                sentences = list(map(normalize, line.split("\t")))
                pair = Pair(
                    input_=sentences[0],
                    target=sentences[1]
                )
                pairs.append(pair)
        
        if reverse:
            for pair in pairs:
                tmp = pair.input_
                pair.input_ = pair.target
                pair.target = tmp
            input_lang = Lang(lang2)
            output_lang = Lang(lang1)
        else:
            input_lang = Lang(lang1)
            output_lang = Lang(lang2)
        
        return input_lang, output_lang, pairs
