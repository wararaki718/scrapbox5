from pydantic import BaseModel

from .estimator import EstimatorConfig
from .vectorizer import VectorizerConfig


class PredictorConfig(BaseModel):
    estimator_config: EstimatorConfig
    vectorizer_config: VectorizerConfig
