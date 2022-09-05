from dataclasses import dataclass
from typing import Optional, Set

import numpy as np


@dataclass
class Node:
    index: int
    data: Optional[np.ndarray] = None
    friends: Optional[Set[int]] = None


@dataclass
class NodeDistCloser:
    node: Node
    distance: float

    def __lt__(self, node: "NodeDistCloser") -> bool:
        return self.distance < node.distance
