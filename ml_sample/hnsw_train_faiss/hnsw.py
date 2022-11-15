import faiss
import numpy as np


class HNSW:
    def __init__(self, dim: int, n_nn: int):
        self._index = faiss.IndexHNSWFlat(dim, n_nn)
    
    def train(self, x: np.ndarray):
        self._index.train(x)
    
    def add(self, x: np.ndarray):
        self._index.add(x)
    
    @property
    def is_trained(self) -> bool:
        return self._index.is_trained
    
    def search(self, x: np.ndarray, k: int=10) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances
