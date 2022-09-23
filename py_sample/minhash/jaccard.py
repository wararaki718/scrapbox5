import numpy as np

from minhash import MinHash


def jaccard(x: MinHash, y: MinHash) -> float:
    return float(np.count_nonzero(x.values == y.values)) / float(len(x))
