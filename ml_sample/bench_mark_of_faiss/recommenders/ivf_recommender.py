import faiss
import numpy as np

from .base_recommender import BaseRecommender


class IVFRecommender(BaseRecommender):
    def __init__(self, dim: int, n_centroids: int, n_bits: int):
        quantizer = faiss.IndexFlatL2(dim)
        self._index = faiss.IndexIVFPQ(quantizer, dim, n_centroids, n_bits, 8)
    
    def add(self, x: np.ndarray):
        self._index.train(x)
        self._index.add(x)
    
    def search(self, x: np.ndarray, k: int=10) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances, indices
