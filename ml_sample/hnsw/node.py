from dataclasses import dataclass, field
from typing import Optional, Set

import numpy as np


@dataclass
class Node:
    index: int
    data: Optional[np.ndarray] = None
    neighbors: Set["Node"] = field(default_factory=set)

    def __lt__(self, node: "Node") -> bool:
        return self.index < node.index
    
    def __eq__(self, node: "Node") -> bool:
        return self.index == node.index


@dataclass
class NodeDistCloser:
    node: Node
    distance: float

    def __lt__(self, node: "NodeDistCloser") -> bool:
        return self.distance < node.distance
    
    def __str__(self) -> str:
        return f"index={self.node.index}, distance={self.distance}"
