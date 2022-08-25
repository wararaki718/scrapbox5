import faiss
import numpy as np

from .base_recommender import BaseRecommender


class HNSWFlatRecommender(BaseRecommender):
    def __init__(self, dim: int, n_nn: int):
        self._index = faiss.IndexHNSWFlat(dim, n_nn)
    
    def add(self, x: np.ndarray):
        self._index.add(x)
    
    def search(self, x: np.ndarray, k: int=10) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances, indices
