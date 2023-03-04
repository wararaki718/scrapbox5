import numpy as np
from sklearn.linear_model import LogisticRegression


class SurviverClassifier:
    def __init__(self):
        self._model = LogisticRegression()
    
    def fit(self, x: np.ndarray, y: np.ndarray):
        self._model.fit(x, y)
