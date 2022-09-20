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
    
    def search(self, query: np.ndarray, k: int=5, n_probes: int=5) -> Tuple[np.ndarray, np.ndarray]:
        distances = self._model.transform(query.reshape(1, -1))[0]
        indices = np.argsort(distances)[:n_probes]
        x = np.vstack(
            [
                np.array(self._posting_list[index])
                for index in indices
            ]
        )
        distances = np.linalg.norm(x - query, axis=1)
        indices = np.argsort(distances)[:k]
        return indices, distances[indices]
