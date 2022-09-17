import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.vq import vq
from scipy.spatial.distance import cdist


class PQ:
    def __init__(self, n_clusters: int, m: int) -> None:
        self._n_clusters = n_clusters
        self._m = m
    
    def fit(self, x: np.ndarray):
        d_sub = int(x.shape[1] / self._m)
        
        self._codebook = np.empty((self._m, self._n_clusters, d_sub), np.float32)
        for m in range(self._m):
            x_sub = x[:, m*d_sub:(m+1)*d_sub]
            model = KMeans(self._n_clusters)
            model.fit(x_sub)
            self._codebook[m] = model.cluster_centers_
    
    def encode(self, x: np.ndarray) -> np.ndarray:
        d_sub = self._codebook.shape[2]
        codes = np.empty((x.shape[0], self._m), np.uint8)
        for m in range(self._m):
            x_sub = x[:, m*d_sub:(m+1)*d_sub]
            codes[:, m], _ = vq(x_sub, self._codebook[m])

        return codes

    def search(self, codes: np.ndarray, query: np.ndarray) -> np.ndarray:
        d_sub = self._codebook.shape[2]

        table = np.empty((self._m, self._n_clusters), np.float32)
        for m in range(self._m):
            q_sub = query[m*d_sub:(m+1)*d_sub]
            table[m, :] = cdist([q_sub], self._codebook[m], "sqeuclidean")[0]
        
        dist = np.sum(table[range(self._m), codes], axis=1)
        return dist
