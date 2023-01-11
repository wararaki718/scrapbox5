from typing import Tuple

import numpy as np
from sklearn.datasets import load_svmlight_file


class DataLoader:
    def load(self, filename: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        X_train, y_train = load_svmlight_file(f"dataset/{filename}")
        q_train = np.loadtxt(f"dataset/{filename}.query")
        return X_train, y_train, q_train
