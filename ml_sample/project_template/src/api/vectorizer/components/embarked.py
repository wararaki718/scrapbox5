from pathlib import Path

import joblib
import numpy as np


class EmbarkedVectorizer:
    def __init__(self, model_path: Path):
        self._vectorizer = joblib.load(model_path)

    def transform(self, embarkeds: np.ndarray) -> np.ndarray:
        x = self._vectorizer.transform(embarkeds)
        return x
