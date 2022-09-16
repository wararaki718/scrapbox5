from typing import List

import numpy as np

from node import Node
from utils import distance


def greedy_search(q: np.ndarray, node: Node) -> Node:
    d_min = distance(q, node.vector)
    node_next = None

    for neighbor in node.neighbors:
        d = distance(q, neighbor.vector)
        if d < d_min:
            node_next = neighbor
            d_min = d
    
    if node_next is None:
        return node
    
    return greedy_search(q, node_next)


def search(q: np.ndarray, nodes: List[Node]) -> Node:
    entry_point = np.random.choice(nodes)
    return greedy_search(q, entry_point)
