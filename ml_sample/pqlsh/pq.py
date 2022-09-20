import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.vq import vq


class PQ:
    def __init__(self, n_clusters: int, m: int) -> None:
        """
        n_clusters: the number of k-means cluster
        m: partition size
        """
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
    
    def fit_encode(self, x: np.ndarray) -> np.ndarray:
        self.fit(x)
        return self.encode(x)
