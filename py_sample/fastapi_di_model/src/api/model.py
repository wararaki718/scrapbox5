from typing import Optional

from .config import Config


class Classifier:
    model: Optional["Classifier"] = None

    def __init__(self, threshold: int):
        self._threshold = threshold

    @classmethod
    def get_model(cls, config: Config) -> "Classifier":
        if cls.model is not None:
            return cls.model

        cls.model = cls(config.threshold)
        print("model loaded")
        return cls.model

    def predict(self, x: int) -> int:
        if x < self._threshold:
            return 0
        else:
            return 1
