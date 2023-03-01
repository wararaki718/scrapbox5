from pathlib import Path

import joblib
from sklearn.base import BaseEstimator


class ModelDumper:
    def __init__(self):
        pass

    def dump(self, model: BaseEstimator, model_path: Path):
        joblib.dump(model, model_path)
