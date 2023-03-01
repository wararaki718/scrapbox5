import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer


class EmbarkedVectorizer:
    def __init__(self):
        self._vectorizer = MultiLabelBinarizer()

    def fit_transform(self, embarkeds: pd.Series) -> np.ndarray:
        x = self._vectorizer.fit_transform(embarkeds.values)
        return x
