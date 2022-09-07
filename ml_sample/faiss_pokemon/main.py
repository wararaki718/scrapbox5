import random
from pathlib import Path

import faiss
import numpy as np

from loader import load_pokemon


def show(names: list, index: int, distances: np.ndarray, indices: np.ndarray):
    print(f"query: {names[index]} [No{index+1}]")
    for i, (ind, distance) in enumerate(zip(indices[1:], distances[1:]), start=1):
        print(f"{i}-th: {names[ind]} [No{ind+1}, distance={distance}]")
    print()


def min_max_scaler(x: np.ndarray) -> np.ndarray:
    x_min = x.min(axis=0, keepdims=True)
    x_max = x.max(axis=0, keepdims=True)
    return (x - x_min) / (x_max - x_min)


def main():
    df = load_pokemon(Path("data/Pokemon.csv"))
    names = df.Name.tolist()
    features = df.drop("Name", axis=1).values.astype(np.float32)
    features = min_max_scaler(features)
    features = np.ascontiguousarray(features, dtype=np.float32)
    print(f"features: {features.shape}")

    x = np.ascontiguousarray(features, dtype=np.float32)
    hnsw = faiss.IndexHNSWFlat(x.shape[1], 24)
    hnsw.add(x)
    print("added features")
    print()

    index = random.randint(0, len(names)-1)
    query = features[index].reshape((1, -1))
    distances, indices = hnsw.search(query, 11)

    show(names, index, distances[0], indices[0])
    print("DONE")


if __name__ == "__main__":
    main()
