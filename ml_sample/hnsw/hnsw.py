from typing import List

import numpy as np

from node import Node, NodeDistCloser
from treeset import TreeSet


def knn_search(nodes: List[Node], query: np.ndarray, k: int, ef: int) -> List[Node]:
    """"
    k: number of nearest neighbor
    ef: size of dynamic candidate
    """
    visits = set()
    candidates = TreeSet() # NodeDistCloser
    results = TreeSet() # NodeDistCloser

    for _ in range(1, ef+1):
        if len(visits) == len(nodes):
            break
        
        # create candidates set
        tmp_results = []
        while True:
            node = np.random.choice(nodes)

            if node.index not in visits:
                visits.add(node.index)
                distance = np.linalg.norm(node.data - query)
                candidates.add(NodeDistCloser(node, distance)) # add node distances
                tmp_results.append(NodeDistCloser(node, distance))
                break
        
        # update list of candidates
        while True:
            if len(candidates) == 0:
                break

            candidate = candidates.poll_first()
            if len(results) >= k:
                result = results[k-1]
                if candidate.distance >= result.distance:
                    break
            
            for f_index in candidate.node.friends:
                node = nodes[f_index]
                if f_index not in visits:
                    visits.add(f_index)
                    distance = np.linalg.norm(node.data - query)
                    candidates.add(NodeDistCloser(node, distance))
                    tmp_results.append(NodeDistCloser(node, distance))
            
        for node in tmp_results:
            results.add(node)

    return [result.node for result in results[1:]]

def insert(nodes: List[Node], node: Node, f: int, w: int):
    neighbors = knn_search(nodes, node.data, w, f)
    for neighbor in neighbors:
        neighbor.friends.add(node.index)
        node.friends.add(neighbor.index)


def build_index(nodes: List[Node], f: int, w: int):
    for node in nodes:
        insert(nodes, node, f, w)


def greedy_search(nodes: List[Node], q: np.ndarray) -> Node:
    nearest_node = np.random.choice(nodes)
    nearest_distance = np.linalg.norm(nearest_node.data - q)

    while True:
        break_search = True
        for friend in nearest_node.friends:
            distance = np.linalg.norm(friend.data - q)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_node = friend
                break_search = False
        
        if break_search:
            break
    
    return nearest_node

