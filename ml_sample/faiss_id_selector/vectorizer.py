import numpy as np


class PokemonVectorizer:
    def __init__(self):
        pass

    def transform(self, X: np.ndarray) -> np.ndarray:
        # min-max scaler
        X_min = X.min(axis=0, keepdims=True)
        X_max = X.max(axis=0, keepdims=True)
        X_new = (X - X_min) / (X_max - X_min)
        return np.ascontiguousarray(X_new, dtype=np.float32)
