from typing import List

import numpy as np

from layer import Layer
from ml_sample.hnsw.treeset import TreeSet
from node import Node, NodeDistCloser
from search_layer import search_layer
from select_neighbors import select_neighbors_simple
from treeset import TreeSet
from utils import random_level


# ref: https://github.com/rust-cv/hnsw/blob/master/src/hnsw/hnsw_const.rs#L144
def insert(layers: List[Layer], q: np.ndarray, m: int, m_max: int, ef: int, ml: int):
    """
    layers: multilayer graph
    q: new element of data
    m: number of established connections
    m_max: maximum number of connections for each element per layer
    ef: size of the dynamic candidate list
    ml: normalization factor for level generation
    """
    # implement empty case
    # 1. first insert
    # 2. create new layer
    level = random_level(ml)
    l_ep = len(layers)
    ep = layers[-1].nodes[-1]
    
    for lc in range(len(layers), level):
        w = search_layer(q, ep, 1, layers[lc])
        ep = w.first().node
    
    for lc in reversed([i for i in range(min(level, l_ep))]):
        w = search_layer(q, ep, ef, lc)
        candidates = [item.node for item in w]
        neighbors = select_neighbors_simple(q, candidates, m)
        # add bidirectional connections
        for neighbor in neighbors:
            pass