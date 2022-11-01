import numpy as np
from typing import List


def spearman(rank_a: List[int], rank_b: List[int]) -> float:
    a = np.array(rank_a)
    b = np.array(rank_b)

    n = len(rank_a)

    r = 1 - (6*np.sum(np.power(a - b, 2)))/(n*(n*n-1))
    return r
