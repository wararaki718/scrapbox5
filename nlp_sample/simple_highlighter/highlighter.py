from typing import List

from adjuster import PositionAdjuster
from indexer import CharacterIndexer
from model import Position
from normalizer import CharacterNormalizer
from searcher import PositionSearcher


class Highlighter:
    def __init__(self):
        self._indexer = CharacterIndexer()
        self._normalizer = CharacterNormalizer()
        self._searcher = PositionSearcher()
        self._adjuster = PositionAdjuster()

    def highlight(self, keywords: List[str], text: str) -> List[Position]:
        text_tokens = self._indexer.index(text)
        text_tokens = self._normalizer.normalize(text_tokens)
        results = []
        for keyword in keywords:
            keyword_tokens = self._indexer.index(keyword)
            keyword_tokens = self._normalizer.normalize(keyword_tokens)
            positions = self._searcher.search(keyword_tokens, text_tokens)
            positions = self._adjuster.adjust(positions, text)
            results.extend(positions)
        return results
