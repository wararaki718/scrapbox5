import numpy as np

from node import Node


def show(node: Node):
    print(f"data: {node.data}, friends: {str(node.friends)}")


def euclidean(x: np.ndarray, y: np.ndarray) -> float:
    return np.linalg.norm(x - y)
