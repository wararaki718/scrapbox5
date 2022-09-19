from collections import defaultdict
from typing import Tuple

import numpy as np
from sklearn.cluster import KMeans


class IVF:
    def __init__(self, n_clusters: int):
        self._model = KMeans(n_clusters=n_clusters)
        self._posting_list = defaultdict(list)

    def fit(self, x: np.ndarray):
        y_preds = self._model.fit_predict(x)
        for x_, y_pred in zip(x, y_preds):
            self._posting_list[y_pred].append(x_.tolist())
    
    def search(self, query: np.ndarray, k: int=5) -> Tuple[np.ndarray, np.ndarray]:
        y_pred = self._model.predict(query.reshape(1, -1))[0]
        x = np.array(self._posting_list[y_pred])
        distances = np.linalg.norm(x - query, axis=1)
        indices = np.argsort(distances)[:k]
        return indices, distances[indices]
