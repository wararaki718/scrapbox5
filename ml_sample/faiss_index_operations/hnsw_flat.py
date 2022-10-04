import faiss
import numpy as np


class HNSWFlatRecommender:
    def __init__(self, dim: int, n_nn: int):
        self._index = faiss.IndexHNSWFlat(dim, n_nn)
    
    def add(self, x: np.ndarray):
        self._index.add(x)
    
    def search(self, x: np.ndarray, k: int=10) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances, indices
    
    def write(self, filename: str):
        faiss.write_index(self._index, filename)

    def read(self, filename: str):
        self._index = faiss.read_index(filename)
