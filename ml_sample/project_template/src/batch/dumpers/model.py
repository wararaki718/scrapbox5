from pathlib import Path
from typing import Any

import joblib

#from ..estimator import SurviverClassifier


class ModelDumper:
    def __init__(self):
        pass

    def dump(self, classifier: Any, model_path: Path):
        joblib.dump(classifier._model, model_path)
