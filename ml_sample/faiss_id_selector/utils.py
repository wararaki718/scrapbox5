import faiss
import numpy as np


def show(names: list, index: int, distances: np.ndarray, indices: np.ndarray):
    print(f"query: {names[index]} [No{index+1}]")
    for i, (ind, distance) in enumerate(zip(indices[1:], distances[1:]), start=1):
        print(f"{i}-th: {names[ind]} [No{ind+1}, distance={distance}]")
    print()


def show_status(hnsw: faiss.IndexHNSWFlat):
    print(f"max_level: {hnsw.hnsw.max_level}")
    for i in range(hnsw.hnsw.max_level, -1, -1):
        hnsw.hnsw.print_neighbor_stats(i)
        print()
    print()
