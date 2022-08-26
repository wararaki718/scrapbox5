import faiss
import numpy as np

from .base_recommender import BaseRecommender


class PQRecommender(BaseRecommender):
    def __init__(self, dim: int, n_subquantizers: int, n_bits: int):
        self._index = faiss.IndexPQ(dim, n_subquantizers, n_bits)
    
    def add(self, x: np.ndarray):
        self._index.train(x)
        self._index.add(x)
    
    def search(self, x: np.ndarray, k: int=10) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances, indices
