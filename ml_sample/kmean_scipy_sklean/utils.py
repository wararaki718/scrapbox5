import numpy as np


def get_data(n: int, dim: int) -> np.ndarray:
    x = np.random.random((n, dim)).astype(np.float32)
    return x
