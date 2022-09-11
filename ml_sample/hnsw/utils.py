import numpy as np

from node import Node


def show(node: Node):
    print(f"data: {node.data}, friends: {str(node.friends)}")


def euclidean(x: np.ndarray, y: np.ndarray) -> float:
    return np.linalg.norm(x - y)


def random_level(ml: float) -> int:
    uniform = np.random.uniform()
    return int(np.floor(-np.log(uniform)*(1/np.log(ml))))


if __name__ == "__main__":
    for i in range(2, 6):
        lv = random_level(i)
        print(lv)
