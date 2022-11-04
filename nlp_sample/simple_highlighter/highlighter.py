from typing import List

from indexer import CharacterIndexer
from normalizer import CharacterNormalizer
from schema import Position
from searcher import PositionSearcher


class Highlighter:
    def __init__(self):
        self._indexer = CharacterIndexer()
        self._normalizer = CharacterNormalizer()
        self._searcher = PositionSearcher()

    def highlight(self, keywords: List[str], text: str) -> List[Position]:
        text_tokens = self._indexer.index(text)
        norm_text_tokens = self._normalizer.normalize(text_tokens)
        results = []
        for keyword in keywords:
            # search original
            keyword_tokens = self._indexer.index(keyword)
            positions = self._searcher.search(keyword_tokens, text_tokens)

            # search norm
            norm_keyword_tokens = self._normalizer.normalize(keyword_tokens)
            norm_positions = self._searcher.search(norm_keyword_tokens, norm_text_tokens)
            
            positions = list(set(positions)|set(norm_positions))
            positions.sort()
            results.extend(positions)
        return results
