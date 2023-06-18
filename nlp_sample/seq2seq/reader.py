import re
import unicodedata
from pathlib import Path
from typing import List, Tuple

from schema.lang import Lang


def normalize(s: str) -> str:
    text = unicodedata.normalize("NFKC", s)
    text = text.lower().strip()
    text = re.sub(r"([.!?])", r" \1", text)
    return text.strip()


class LangReader:
    def __init__(self) -> None:
        pass

    def read(self, filename: Path, lang1: str, lang2: str, reverse: bool=False) -> Tuple[Lang, Lang, List[List[str]]]:
        pairs: List[List[str]] = []
        with open(filename) as f:
            for line in f:
                pair = list(map(normalize, line.split("\t")))
                pairs.append(pair)
        
        if reverse:
            pairs = [list(reversed(pair)) for pair in pairs]
            input_lang = Lang(lang2)
            output_lang = Lang(lang1)
        else:
            input_lang = Lang(lang1)
            output_lang = Lang(lang2)
        
        return input_lang, output_lang, pairs
