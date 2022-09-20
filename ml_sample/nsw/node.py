from dataclasses import dataclass, field
from typing import Set

import numpy as np


@dataclass
class Node:
    index: int
    vector: np.ndarray
    neighbors: Set["Node"] = field(default_factory=set)

    def contains(self, node: "Node") -> bool:
        for neighbor in self.neighbors:
            if neighbor.index == node.index:
                return True
        return False


@dataclass
class NodeDistCloser:
    node: Node
    distance: float

    def __lt__(self, node: "NodeDistCloser") -> bool:
        return self.distance < node.distance
