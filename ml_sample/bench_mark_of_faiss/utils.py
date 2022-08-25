import numpy as np


def get_data(n: int, d: int) -> np.ndarray:
    x = np.random.random((n, d)).astype(np.float32)
    x[:, 0] += np.arange(n) / 1000
    return x
