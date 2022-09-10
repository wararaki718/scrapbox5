from typing import List

import numpy as np

from layer import Layer
from node import Node
from search_layer import search_layer


def knn_search(layers: List[Layer], q: np.ndarray, k: int, ef: int) -> List[Node]:
    """
    layers: multilayer graph
    q: query element
    k: number of neighbors to return
    ef: size of dynamic candidate list
    """
    ep = np.random.choice(layers[0])
    for layer in layers[:-1]:
        results = search_layer(q, ep, 1, layer)
        ep = results.poll_first().node
    results = search_layer(q, ep, ef, layers[-1])

    return [result.node for result in results[:k]]
