from queue import PriorityQueue
from typing import List

import numpy as np

from node import Node


class KNN:
    def __init__(self, k: int, ef: int):
        self._k = k # number of nearest neighbor
        self._ef = ef # size of dynamic candidate

    def search(self, nodes: List[Node], query: np.ndarray) -> List[Node]:
        visits = set()
        candidates = PriorityQueue(self._ef)
        result = PriorityQueue(self._ef)

        for _ in range(1, self._ef+1):
            if len(visits) == len(nodes):
                break
            
            # create candidates set
            tmp_results = []
            while True:
                index = np.random.randint(0, len(nodes)-1)
                node = nodes[index]
                if index not in visits:
                    visits.add(index)
                    candidates.put() # add node distances
                    tmp_results.add() # add
                    break
            
            # update list of candidates
            

