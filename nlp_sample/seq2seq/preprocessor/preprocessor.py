from typing import List, Tuple

from .pair import PairFilter
from schema.lang import Lang
from schema.pair import Pair


class Preprocessor:
    def __init__(self) -> None:
        self._pair_filter = PairFilter()
    
    def transform(self, input_lang: Lang, output_lang: Lang, pairs: List[Pair]) -> Tuple[Lang, Lang, List[Pair]]:
        pairs = self._pair_filter.filter(pairs)
        for pair in pairs:
            input_lang.add(pair.input_)
            output_lang.add(pair.target)
        
        return input_lang, output_lang, pairs
