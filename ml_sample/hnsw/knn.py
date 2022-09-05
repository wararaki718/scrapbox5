from typing import List, Tuple

import numpy as np

from node import Node, NodeDistCloser
from result import Result
from treeset import TreeSet


class KNN:
    def __init__(self, k: int, ef: int):
        self._k = k # number of nearest neighbor
        self._ef = ef # size of dynamic candidate

    def search(self, nodes: List[Node], query: np.ndarray) -> List[Result]:
        visits = set()
        candidates = TreeSet() # NodeDistCloser
        results = TreeSet() # NodeDistCloser

        for _ in range(1, self._ef+1):
            if len(visits) == len(nodes):
                break
            
            # create candidates set
            tmp_results = []
            while True:
                node = np.random.choice(nodes)

                if node.index not in visits:
                    visits.add(node.index)
                    distance = np.linalg.norm(node.data, query)
                    candidates.add(NodeDistCloser(node, distance)) # add node distances
                    tmp_results.append(NodeDistCloser(node, distance))
                    break
            
            # update list of candidates
            while True:
                if len(candidates) == 0:
                    break

                candidate = candidates.poll_first()
                if len(results) >= self._k:
                    result = results[self._k]
                    if candidate.distance >= result.distance:
                        break
                
                for f_index in candidate.node.friends:
                    node = nodes[f_index]
                    if f_index not in visits:
                        visits.add(f_index)
                        distance = np.linalg.norm(node.data, query)
                        candidates.add(NodeDistCloser(node, distance))
                        tmp_results.append(NodeDistCloser(node, distance))
                
            for node in tmp_results:
                results.add(Result(node.index, node.distance))

        return results[1:]