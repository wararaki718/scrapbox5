import numpy as np


def distance(x: np.ndarray, y: np.ndarray) -> float:
    return np.linalg.norm(x - y)
