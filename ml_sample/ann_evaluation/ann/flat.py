import faiss
import numpy as np

from .base import Base
from metric_type import MetricType


class Flat(Base): # inner product
    def __init__(self, n_dimensions: int, metric_type: MetricType = MetricType.IP):
        if metric_type == MetricType.IP:
            self._index = faiss.IndexFlatIP(n_dimensions)
        elif metric_type == MetricType.L2:
            self._index = faiss.IndexFlatL2(n_dimensions)
        else:
            raise TypeError(f"metric_type error")

    def add(self, x: np.ndarray):
        self._index.add(x)
    
    def search(self, x: np.ndarray, k: int=10) -> tuple:
        distances, indices = self._index.search(x, k)
        return distances, indices
