from typing import List, Optional, Tuple

import numpy as np

from layer import Layer
from node import Node
from search_layer import search_layer
from select_neighbors import select_neighbors_simple
from utils import random_level


def _init(layers: List[Layer], index: int, vector: np.ndarray):
    node = Node(index=index, data=vector)
    layer = Layer(node=[node])
    layers.append(layer)


def _add(layers: List[Layer], node: Node, nodes: List[Node], level: int):
    if len(layers) <= level:
        layers.append()


# ref: https://github.com/rust-cv/hnsw/blob/master/src/hnsw/hnsw_const.rs#L144
def insert(data: np.ndarray,
           layers: List[Layer],
           q_index: np.ndarray,
           ep: Optional[Node],
           ep_level: int,
           m: int,
           m_max: int,
           ef: int,
           ml: int) -> Tuple[Node, int]:
    """
    data: data
    layers: multilayer graph
    q_index: new element index
    m: number of established connections
    m_max: maximum number of connections for each element per layer
    ef: size of the dynamic candidate list
    ml: normalization factor for level generation
    """
    # implement empty case
    # 1. first insert
    # 2. create new layer
    level = random_level(ml)

    if len(layers) == 0:
        _init(layers, q_index, data[q_index])
        return layers[0][0], 0
    
    for lc in range(len(layers), level):
        w = search_layer(data[q_index], ep, 1, layers[lc])
        ep = w.first().node
    
    for lc in reversed([i for i in range(min(level, ep_level))]):
        w = search_layer(data[q_index], ep, ef, lc)
        candidates = [item.node for item in w]
        neighbors = select_neighbors_simple(data[q_index], candidates, m)

        # todo: add bidirectional connections
    
        for neighbor in neighbors:
            if len(neighbor.neighbors) > m_max:
                new_neighbors = select_neighbors_simple(neighbor, neighbor.neighbors, m_max, lc)
                for new_neighbor in new_neighbors:
                    pass
    
    return ep, ep_level
