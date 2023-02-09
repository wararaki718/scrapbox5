from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Node:
    children: Dict[str, "Node"] = field(default_factory=dict)
    char: str = ""

    def has(self, c) -> bool:
        return c in self.children

    def next(self, c: str) -> str:
        return self.children[c]

    def next_all(self) -> List["Node"]:
        return list(self.children.values())

    def add(self, c: str):
        self.children[c] = Node(char=c)

    def is_empty(self) -> bool:
        return len(self.children) == 0
