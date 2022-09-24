from collections import defaultdict

from minhash import MinHash


class LSH:
    def __init__(self, n_perm: int=128, threshold: float=0.9):
        self._r = 32
        self._b = int(n_perm/self._r)
        self._tables = [
            defaultdict(set)
            for _ in range(self._b)
        ]
        self._keys = defaultdict(set)
        self._buffer_size = 5000
        self._n_perm = n_perm
        self._threshold = threshold
    
    def insert(self, key: str, minhash: MinHash):
        hs = [
            bytes(minhash.values[i*self._r:(i+1)*self._r].byteswap().data)
            for i in range(self._b)
        ]
        self._keys[key].update(*hs)
        for h, table in zip(hs, self._tables):
            table[key].update(h)
    
    def query(self, q: MinHash) -> set:
        results = set()
        for i, table in enumerate(self._tables):
            h = bytes(q.values[i*self._r:(i+1)*self._r].byteswap().data)
            for key in table.get(h, set()):
                results.add(key)
        return results
