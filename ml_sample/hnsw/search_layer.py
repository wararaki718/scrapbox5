import numpy as np

from layer import Layer
from node import Node, NodeDistCloser
from treeset import TreeSet
from utils import euclidean


# ref: https://arxiv.org/pdf/1603.09320.pdf
# ref: https://github.com/rust-cv/hnsw/blob/master/src/hnsw/hnsw_const.rs#L183
def search_layer(q: np.ndarray, ep: Node, ef: int, layer: Layer) -> TreeSet:
    """
    q: query element
    ep: entry point
    ef: number of nearest neighbors
    layer: layer
    """
    visited = set([ep.index])
    candidates = TreeSet([NodeDistCloser(ep, euclidean(ep.data, q))])
    neighbors = TreeSet([NodeDistCloser(ep, euclidean(ep.data, q))])

    while len(candidates) > 0:
        candidate: Node = candidates.poll_first().node
        furthest: Node = neighbors.last().node

        if euclidean(candidate.data, q) > euclidean(furthest.data, q):
            break
        
        for neighbor in layer.nodes: # set layers[lc].candidate.neighbors
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


if __name__ == "__main__":
    dim = 2
    k = 5
    query = np.random.random(dim)
    nodes = [Node(index=i, data=np.random.random(dim)) for i in range(20)]
    ep = np.random.choice(nodes)
    layer = Layer(nodes=nodes)

    results = search_layer(query, ep, k, layer)
    print(f"ep: index={ep.index}")
    for result in results:
        print(result)
    print("DONE")
