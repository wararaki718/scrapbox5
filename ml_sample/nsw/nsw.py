import numpy as np

from greedy import search
from insert import build
from node import Node


class NSW:
    def __init__(self, f: int, w: int):
        """
        f: number of cloest elements
        w: the number of search
        """
        self._f = f
        self._w = w

    def add(self, vectors: np.ndarray):
        self._nodes = [
            Node(index=i, vector=vector)
            for i, vector in enumerate(vectors)
        ]
        build(self._nodes, self._f, self._w)

    def get_neighbor(self, q: np.ndarray) -> Node:
        return search(q, self._nodes)
