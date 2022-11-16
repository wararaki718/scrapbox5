import faiss
import numpy as np

from .base import Base
from metric_type import MetricType


class HNSW(Base):
    def __init__(self,
                 n_dimensions: int,
                 n_nearest_neigbhors: int,
                 metric_type: MetricType=MetricType.L2):
        self._index = faiss.IndexHNSWFlat(
            n_dimensions,
            n_nearest_neigbhors,
            metric_type.value
        )
    
    def add(self, x: np.ndarray):
        self._index.add(x)
    
    def search(self, x: np.ndarray, k: int=10) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances, indices
