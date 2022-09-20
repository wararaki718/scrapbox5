from typing import List

import numpy as np
from datasketch import MinHash, MinHashLSH

from pq import PQ


class PQLSH:
    def __init__(self, n_clusters: int, m: int, n_perm: int, threshold: float=0.5):
        self._quantizer = PQ(n_clusters, m)
        self._lsh = MinHashLSH(num_perm=n_perm, threshold=threshold)
        self._n_perm = n_perm
    
    def _get_minhash(self, x: np.ndarray) -> MinHash:
        # x: 1-d array
        m = MinHash(num_perm=self._n_perm)
        for x_ in x:
            m.update(x_.tobytes()) # np.uint8
        return m

    def add(self, x: np.ndarray):
        # x: 2-d array
        X_encoded = self._quantizer.fit_encode(x)
        for index, x_encoded in enumerate(X_encoded):
            m = self._get_minhash(x_encoded)
            self._lsh.insert(f"m{index}", m)

    def search(self, query: np.ndarray, k: int=10) -> List[str]:
        # query: 1-d array
        x = self._quantizer.encode(query.reshape((1, -1)))[0]
        m = self._get_minhash(x)
        results = self._lsh.query(m)[:k]
        return results
