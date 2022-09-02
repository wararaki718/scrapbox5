from functools import partial

import numpy as np
from scipy.cluster.vq import kmeans2, vq


class SCKMeans:
    def __init__(self,
                 n_clusters: int,
                 n_iter: int=10,
                 thresh: float=1e-5,
                 minit: str="random",
                 missing: str="warn",
                 check_finite: bool=True):
        self._model = partial(
            kmeans2,
            k=n_clusters,
            iter=n_iter,
            thresh=thresh,
            minit=minit,
            missing=missing,
            check_finite=check_finite
        )
    
    def fit(self, x: np.ndarray):
        self._centroids, self._labels = self._model(data=x)
    
    def predict(self, x: np.ndarray) -> np.ndarray:
        labels, _ = vq(x, self._centroids) # labels, distances
        return labels
