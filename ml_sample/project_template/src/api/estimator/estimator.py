import joblib
import numpy as np

from api.schema.config import EstimatorConfig


class SurviveEstimator:
    def __init__(self, estimator_config: EstimatorConfig):
        self._model = joblib.load(estimator_config.model_path)
    
    def estimate(self, x: np.ndarray) -> np.ndarray:
        return self._model.predict(x)
