from collections import defaultdict
from typing import Tuple

import numpy as np
from sklearn.cluster import KMeans


class IVF:
    def __init__(self, n_clusters: int):
        self._model = KMeans(n_clusters=n_clusters)
        self._posting_list_data = defaultdict(list)
        self._posting_list_index = defaultdict(list)

    def fit(self, x: np.ndarray):
        y_preds = self._model.fit_predict(x)
        for i, (x_, y_pred) in enumerate(zip(x, y_preds)):
            self._posting_list_data[y_pred].append(x_.tolist())
            self._posting_list_index[y_pred].append(i)
    
    def search(self, query: np.ndarray, k: int=5, n_probes: int=5) -> Tuple[np.ndarray, np.ndarray]:
        cdistances = self._model.transform(query.reshape(1, -1))[0]
        clusters = np.argsort(cdistances)[:n_probes]
        x = np.vstack(
            [
                np.array(self._posting_list_data[cluster])
                for cluster in clusters
            ]
        )
        indices = np.hstack(
            [
                np.array(self._posting_list_index[cluster])
                for cluster in clusters
            ]
        )
        distances = np.linalg.norm(x - query, axis=1)
        results = np.argsort(distances)[:k]
        return indices[results], distances[results]
