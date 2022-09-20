from typing import List

from knn import knn_search
from node import Node


def insert(nodes: List[Node], new_node: Node, f: int, w: int):
    neighbors = knn_search(nodes, new_node.vector, w, f)
    for neighbor in neighbors:
        if not neighbor.contains(new_node):
            neighbor.neighbors.add(new_node)
            new_node.neighbors.add(neighbor)


def build(nodes: List[Node], f: int, w: int):
    for node in nodes:
        insert(nodes, node, f, w)
