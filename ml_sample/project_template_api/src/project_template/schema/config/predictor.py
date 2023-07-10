from pydantic import BaseModel

from .estimator import EstimatorConfig
from .vectorizer import VectorizerConfig


class SurvivePredictorConfig(BaseModel):
    estimator_config: EstimatorConfig
    vectorizer_config: VectorizerConfig


class PredictorConfig(BaseModel):
    survive_predictor_config: SurvivePredictorConfig
