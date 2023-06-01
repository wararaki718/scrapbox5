from dataclasses import dataclass, field
from typing import Dict, List, Sequence


@dataclass
class Node:
    children: Dict[str, "Node"] = field(default_factory=dict)
    char: str = ""

    def has(self, c) -> bool:
        return c in self.children

    def next(self, c: str) -> "Node":
        return self.children[c]

    def next_all(self) -> List["Node"]:
        return list(self.children.values())

    def add(self, c: str) -> None:
        self.children[c] = Node(char=c)

    def is_empty(self) -> bool:
        return len(self.children) == 0


class TrieTreeSuggester:
    _root: Node
    
    def __init__(self) -> None:
        self._root = Node()

    def _insert(self, text: str) -> None:
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

    def index(self, suggestions: Sequence[str]) -> None:
        for s in suggestions:
            self._insert(s)

    def search(self, text: str) -> List[str]:
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
