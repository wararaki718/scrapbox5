from project_template.schema.config import PredictorConfig
from project_template.schema.request import Passenger
from project_template.survive.predictor import SurvivePredictor


class Predictor:
    def __init__(self, config: PredictorConfig) -> None:
        self._survive_predictor = SurvivePredictor(config.survive_predictor_config)
    
    def predict(self, passenger: Passenger) -> int:
        return self._survive_predictor.predict(passenger)
