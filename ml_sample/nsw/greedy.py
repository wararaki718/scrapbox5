from typing import List

import numpy as np

from node import Node
from utils import distance


def search(q: np.ndarray, node: Node) -> Node:
    d_min = distance(q, node.vector)
    node_next = None

    for neighbor in node.neighbors:
        d = distance(q, neighbor.vector)
        if d < d_min:
            node_next = neighbor
            d_min = d
    
    if node_next is None:
        return node
    
    return search(q, node_next)
