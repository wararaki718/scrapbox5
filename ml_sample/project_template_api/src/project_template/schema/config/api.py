from pathlib import Path

import yaml
from pydantic import BaseModel

from .predictor import PredictorConfig


class APIConfig(BaseModel):
    predictor_config: PredictorConfig

    @classmethod
    def load(cls, config_path: Path) -> "APIConfig":
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return cls(**config)
