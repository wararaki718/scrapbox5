import numpy as np

from node import Node, NodeDistCloser
from treeset import TreeSet
from utils import euclidean


# ref: https://github.com/rust-cv/hnsw/blob/master/src/hnsw/hnsw_const.rs#L183
def search_layer(q: np.ndarray, ep: Node, ef: int, lc: int) -> TreeSet[NodeDistCloser]:
    """
    q: query element
    ep: entry point
    ef: number of nearest neighbors
    lc: layer number
    """
    visited = set([ep.index])
    candidates = TreeSet([NodeDistCloser(ep, euclidean(ep.data, q))])
    neighbors = TreeSet([NodeDistCloser(ep, euclidean(ep.data, q))])

    while len(candidates) > 0:
        candidate: Node = candidates.poll_first().node
        furthest: Node = neighbors.last().node

        if euclidean(candidate.data, q) > euclidean(furthest.data, q):
            break
        
        for neighbor in candidate.neighbors: # set layers[lc].candidate.neighbors
            if neighbor.index in visited:
                continue

            visited.add(neighbor.index)
            furthest = neighbors.last().node

            if euclidean(neighbor.data, q) < euclidean(furthest.data, q) or len(neighbors) < ef:
                candidates.add(NodeDistCloser(neighbor, euclidean(neighbor.data, q)))
                neighbors.add(NodeDistCloser(neighbor, euclidean(neighbor.data, q)))
                if len(neighbors) > ef:
                    _ = neighbors.poll_last()
            
    return neighbors
