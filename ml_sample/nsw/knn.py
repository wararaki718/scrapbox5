from typing import List, Set

import numpy as np

from node import Node, NodeDistCloser
from treeset import TreeSet
from utils import distance


def knn_search(nodes: List[Node], q: np.ndarray, m: int, k: int) -> List[Node]:
    results = TreeSet()
    tmp_results = TreeSet()
    candidates = TreeSet()
    visits = Set[int]

    for _ in range(m):
        entry_point: Node = np.random.choice(nodes)
        candidates.add(
            NodeDistCloser(entry_point, distance(q, entry_point.vector))
        )
        tmp_results.clear()

        while not candidates.is_empty():
            nearest = candidates.poll_first()
            if len(results) >= k and results[k].distance < nearest.distance:
                break
            
            for neighbor in nearest.node.neighbors:
                if neighbor.index not in visits:
                    node = NodeDistCloser(neighbor, distance(q, neighbor.vector))
                    visits.add(neighbor.index)
                    candidates.add(node)
                    tmp_results.add(node)
        
        results.add(tmp_results)
    
    return [result.node for result in results[:k]]
