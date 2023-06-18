from typing import List, Tuple

from .pair import PairFilter
from schema.lang import Lang


class Preprocessor:
    def __init__(self) -> None:
        self._pair_filter = PairFilter()
    
    def transform(self, input_lang: Lang, output_lang: Lang, pairs: List[List[str]]) -> Tuple[Lang, Lang, List[List[str]]]:
        pairs = self._pair_filter.filter(pairs)
        for pair in pairs:
            input_lang.add(pair[0])
            output_lang.add(pair[1])
        
        return input_lang, output_lang, pairs
