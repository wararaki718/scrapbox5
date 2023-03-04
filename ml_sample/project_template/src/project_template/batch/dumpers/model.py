from pathlib import Path

import joblib

from project_template.batch.estimator import SurviverClassifier


class ModelDumper:
    def __init__(self):
        pass

    def dump(self, classifier: SurviverClassifier, model_path: Path):
        joblib.dump(classifier._model, model_path)
