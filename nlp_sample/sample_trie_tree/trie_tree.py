from typing import List

from node import Node


class TrieTree:
    _root: Node
    
    def __init__(self):
        self._root = Node()

    def insert(self, text: str):
        node = self._root
        s = ""
        for c in text:
            s += c
            if not node.has(s):
                node.add(s)
            node = node.next(s)

    def _search(self, prefix: str, node: Node) -> List[str]:
        if node.is_empty():
            return [prefix]

        results = []
        for child in node.next_all():
            results.extend(self._search(child.char, child))        
        return results


    def suggest(self, text: str) -> List[str]:
        # search prefix
        node = self._root
        s = ""
        for c in text:
            s += c
            if not node.has(s):
                return []
            node = node.next(s)
        
        # search suggest
        return self._search(text, node)
