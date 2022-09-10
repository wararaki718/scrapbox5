from typing import List

import numpy as np

from node import Node, NodeDistCloser
from treeset import TreeSet
from utils import euclidean


def select_neighbors_simple(q: np.ndarray, candidates: List[Node], m: int) -> List[Node]:
    """
    q: base element
    candidates: candidate elements
    m: number of neighbors to return m
    """
    neighbors = TreeSet()
    for candidate in candidates:
        neighbors.add(NodeDistCloser(candidate, euclidean(candidate.data, q)))
    
    results = []
    for _ in range(min(m, len(neighbors))):
        results.append(neighbors.poll_first().node)

    return results


def select_neighbors_heuristic(q: np.ndarray, candidates: List[Node], m: int, lc: int, extend_candidates: List[Node], keep_pruned_connections: bool) -> List[Node]:
    results = []
    queue = TreeSet(candidates)

    if len(extend_candidates) > 0:
        for candidate in extend_candidates:
            pass


if __name__ == "__main__":
    dim = 5
    q = np.random.random(dim)
    m = 5
    candidates = [Node(index=i, data=np.random.random(dim)) for i in range(20)]

    results = select_neighbors_simple(q, candidates, m)
    for result in results:
        print(result)
    print("DONE")
