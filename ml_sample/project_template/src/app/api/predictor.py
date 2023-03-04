from .schema.config import PredictorConfig
from .schema.request import Passenger
from .estimator import SurviveEstimator
from .postprocessor import ResultPostprocessor
from .preprocessor import PassengerPreprocessor
from .vectorizer import PassengerVectorizer


class SurvivePredictor:
    def __init__(self, predictor_config: PredictorConfig):
        self._preprocessor = PassengerPreprocessor()
        self._vectorizer = PassengerVectorizer(predictor_config.vectorizer_config)
        self._estimator = SurviveEstimator(predictor_config.estimator_config)
        self._postprocessor = ResultPostprocessor()

    def predict(self, passenger: Passenger) -> int:
        data = self._preprocessor.transform(passenger)
        x = self._vectorizer.transform(data)
        y = self._estimator.estimate(x)
        result = self._postprocessor.transform(y)
        return result
