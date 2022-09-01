import numpy as np
from scipy.cluster.vq import kmeans2, vq
from scipy.spatial.distance import cdist


class PQ:
    def __init__(self, n_clusters: int=256, m: int=4) -> None:
        self._n_clusters = n_clusters
        self._m = m # the size of encoded data
    
    def fit(self, x: np.ndarray):
        ds = int(x.shape[1] / self._m)
        self._codebook = np.empty((self._m, self._n_clusters, ds), np.float32)
        
        for m in range(self._m):
            x_sub = x[:, m*ds:(m+1)*ds]
            self._codebook[m], _ = kmeans2(x_sub, self._n_clusters)

    def encode(self, x: np.ndarray) -> np.ndarray:
        _, _, ds = self._codebook.shape

        codes = np.empty((x.shape[0], self._m), np.uint8)
        for m in range(self._m):
            x_sub = x[:, m*ds:(m+1)*ds]
            codes[:, m], _ = vq(x_sub, self._codebook[m])
        
        return codes
    
    def search(self, codes: np.ndarray, query: np.ndarray) -> np.ndarray:
        _, _, ds = self._codebook.shape
        table = np.empty((self._m, self._n_clusters), np.float32)
        for m in range(self._m):
            query_sub = query[m*ds:(m+1)*ds]
            table[m, :] = cdist([query_sub], self._codebook[m], "sqeuclidean")[0]
        
        dist = np.sum(table[range(self._m), codes], axis=1)
        return dist
