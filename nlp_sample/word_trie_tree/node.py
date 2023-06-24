from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class Node:
    children: Dict[Tuple[str], Tuple["Node"]] = field(default_factory=dict)
    tokens: Tuple[str] = tuple([])

    def has(self, tokens: Tuple[str]) -> bool:
        return tokens in self.children

    def next(self, tokens: Tuple[str]) -> str:
        return self.children[tokens]
    
    def next_all(self) -> List["Node"]:
        return list(self.children.values())

    def add(self, tokens: Tuple[str]) -> None:
        self.children[tokens] = Node(tokens=tokens)
    
    def is_empty(self) -> bool:
        return len(self.children) == 0
