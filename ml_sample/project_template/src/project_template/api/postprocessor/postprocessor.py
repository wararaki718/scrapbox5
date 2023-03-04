import numpy as np


class ResultPostprocessor:
    def __init__(self):
        pass

    def transform(self, y: np.ndarray) -> int:
        result = y[0]
        return result
