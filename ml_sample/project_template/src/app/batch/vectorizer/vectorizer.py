import numpy as np
import pandas as pd

from .components import EmbarkedVectorizer


class TitanicVectorizer:
    def __init__(self):
        self._embarked_vectorizer = EmbarkedVectorizer()

    def fit_transform(self, df: pd.DataFrame) -> np.ndarray:
        return np.hstack([
            df.Pclass.values.reshape(-1, 1),
            df.Age.values.reshape(-1, 1),
            self._embarked_vectorizer.fit_transform(df.Embarked),
            df.Ages.values.reshape(-1, 1)
        ])
