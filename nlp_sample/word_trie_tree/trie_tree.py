from typing import List, Tuple

from node import Node


class TrieTree:
    _root: Node

    def __init__(self) -> None:
        self._root = Node()
    
    def insert(self, tokens: List[str]) -> None:
        node = self._root
        for i, _ in enumerate(tokens, start=1):
            keys = tuple(tokens[:i])
            if not node.has(keys):
                node.add(keys)
            node = node.next(keys)

    def _search(self, tokens: Tuple[str], node: Node) -> List[Tuple[str]]:
        results = [tokens]
        
        for child in node.next_all():
            results.extend(self._search(child.tokens, child))
        return results

    def suggest(self, tokens: List[str]) -> List[Tuple[str]]:
        node = self._root
        for i, _ in enumerate(tokens, start=1):
            keys = tuple(tokens[:i])
            if not node.has(keys):
                return []
            node = node.next(keys)
        
        return self._search(tuple(tokens), node)
