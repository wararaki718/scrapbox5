from collections import defaultdict
from typing import List, Dict

from schema import Character, LinkType


class InvertedIndexer:
    def index(self, tokens: List[Character]) -> Dict[str, List[int]]:
        indices = defaultdict(list)
        for i, token in enumerate(tokens):
            if token.link == LinkType.NODE or token.link == LinkType.TAIL:
                continue
            indices[str(token)].append(i)
        
        return indices
