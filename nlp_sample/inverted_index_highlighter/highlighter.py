from typing import List

from indexer import CharacterIndexer
from inverted_indexer import InvertedIndexer
from normalizer import CharacterNormalizer
from schema import Position
from searcher import PositionSearcher


class Highlighter:
    def __init__(self):
        self._indexer = CharacterIndexer()
        self._inverted_indexer = InvertedIndexer()
        self._normalizer = CharacterNormalizer()
        self._searcher = PositionSearcher()

    def highlight(self, keywords: List[str], text: str) -> List[Position]:
        text_tokens = self._indexer.index(text)
        inverted_indices = self._inverted_indexer.index(text_tokens)
        norm_text_tokens = self._normalizer.normalize(text_tokens)
        norm_inverted_indices = self._inverted_indexer.index(norm_text_tokens)

        results = []
        for keyword in keywords:
            # search original
            keyword_tokens = self._indexer.index(keyword)
            positions = self._searcher.search(keyword_tokens, text_tokens, inverted_indices)

            # search norm
            norm_keyword_tokens = self._normalizer.normalize(keyword_tokens)
            norm_positions = self._searcher.search(norm_keyword_tokens, norm_text_tokens, norm_inverted_indices)
            
            positions = list(set(positions)|set(norm_positions))
            positions.sort()
            results.extend(positions)
        return results
