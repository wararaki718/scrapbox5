from collections import defaultdict

from minhash import MinHash
from optim import optimal_param


class LSH:
    def __init__(self, n_perm: int=128, threshold: float=0.5):
        self._b, self._r = optimal_param(threshold,n_perm)
        self._tables = [
            defaultdict(set)
            for _ in range(self._b)
        ]
        self._keys = defaultdict(set)
        self._buffer_size = 50000
        self._n_perm = n_perm
        self._threshold = threshold
    
    def insert(self, key: str, minhash: MinHash):
        hs = [
            bytes(minhash.values[i*self._r:(i+1)*self._r].byteswap().data)
            for i in range(self._b)
        ]
        self._keys[key].update(*hs)
        for h, table in zip(hs, self._tables):
            table[h].update([key])
    
    def query(self, q: MinHash) -> set:
        results = set()
        for i, table in enumerate(self._tables):
            h = bytes(q.values[i*self._r:(i+1)*self._r].byteswap().data)
            for key in table.get(h, set()):
                results.add(key)
        return results
