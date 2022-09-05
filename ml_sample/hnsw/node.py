from dataclasses import dataclass
import numpy as np


@dataclass
class Node:
    data: np.ndarray
    friends: set


@dataclass
class NodeDistCloser:
    id: int
    distance: float

    def __lt__(self, node: "NodeDistCloser") -> bool:
        return self.distance < node.distance
