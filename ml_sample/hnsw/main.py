import numpy as np

from node import Node
from hnsw import build_index, greedy_search

def main():
    n = 1000
    dim = 2

    nodes = [
        Node(
            index=i,
            data=np.random.random(dim)
        )
        for i in range(n)
    ]

    build_index(nodes, 10, 10)

    q = np.random.random(dim)
    print(f"q: {q}")
    result = greedy_search(nodes, q)
    print(f"result: {result}")
    print()
    print("DONE")


if __name__ == "__main__":
    main()
