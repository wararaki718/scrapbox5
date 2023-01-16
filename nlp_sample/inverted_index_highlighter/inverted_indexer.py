from collections import defaultdict
from typing import List

from schema import Character, InvertedIndex, LinkType


class InvertedIndexer:
    def index(self, tokens: List[Character]) -> InvertedIndex:
        indices = defaultdict(list)
        for i, token in enumerate(tokens):
            if token.link == LinkType.NODE or token.link == LinkType.TAIL:
                continue
            indices[str(token)].append(i)
        
        return InvertedIndex(indices)
