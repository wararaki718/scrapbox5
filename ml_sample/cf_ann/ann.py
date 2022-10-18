import faiss
import numpy as np


class UserAnn:
    def __init__(self, dim: int):
        self._index = faiss.IndexFlatL2(dim)
    
    def add(self, x: np.ndarray):
        self._index.add(x)
    
    def search(self, x: np.ndarray, k: int=5) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances, indices
