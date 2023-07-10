import numpy as np

from .components import EmbarkedVectorizer
from project_template.schema.config import VectorizerConfig
from project_template.schema.data import PreprocessedData


class PassengerVectorizer:
    def __init__(self, config: VectorizerConfig):
        self._embarked_vectorizer = EmbarkedVectorizer(config.vectorizer_path)

    def transform(self, passenger: PreprocessedData) -> np.ndarray:
        return np.hstack([
            np.array(passenger.Pclass),
            np.array(passenger.Age),
            self._embarked_vectorizer.transform(np.array(passenger.Embarked)),
            np.array(passenger.Ages)
        ])
