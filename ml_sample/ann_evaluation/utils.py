import numpy as np

from ann import Base


def get_data(n: int, d: int) -> np.ndarray:
    x = np.random.random((n, d)).astype(np.float32)
    x[:, 0] += np.arange(n) / 1000
    return x


def get_label(
    X_train: np.ndarray,
    X_test: np.ndarray,
    model: Base,
    top_n: int=5) -> np.ndarray:

    model.add(X_train)
    _, y_test = model.search(X_test, k=top_n)

    return y_test
