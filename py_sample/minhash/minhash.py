import numpy as np

from hash import hash

MERSENNE_PRIME = np.uint64((1<<61)-1)
MAX_HASH = np.uint64((1<<32)-1)
HASH_RANGE = (1<<32)


class MinHash:
    def __init__(self, n_perm: int=128, seed: int=42):
        self._n_perm = n_perm
        self._hashvalues = np.ones(n_perm, dtype=np.uint64)*MAX_HASH
        gen = np.random.RandomState(seed)
        self._permutations = np.array([
            (
                gen.randint(1, MERSENNE_PRIME, dtype=np.uint64),
                gen.randint(0, MERSENNE_PRIME, dtype=np.uint64)
            )
            for _ in range(n_perm)
        ], dtype=np.uint64).T

    def update(self, x: bytes):
        i, j = self._permutations
        value = hash(x)
        p = np.bitwise_and((i*value+j)%MERSENNE_PRIME, MAX_HASH)
        self._hashvalues = np.minimum(p, self._hashvalues)
    
    def values(self) -> np.ndarray:
        return self._hashvalues
    
    def __len__(self) -> int:
        return len(self._hashvalues)
