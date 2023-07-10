import joblib
import numpy as np

from project_template.schema.config import EstimatorConfig


class SurviveEstimator:
    def __init__(self, estimator_config: EstimatorConfig):
        #self._model = joblib.load(estimator_config.model_path)
        pass
    
    def estimate(self, x: np.ndarray) -> np.ndarray:
        #return self._model.predict(x)
        return np.array([0] * len(x))
