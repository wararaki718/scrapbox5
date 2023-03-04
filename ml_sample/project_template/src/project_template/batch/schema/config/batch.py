from pathlib import Path

import yaml
from pydantic import BaseModel


class BatchConfig(BaseModel):
    titanic_path: Path
    model_path: Path
    vectorizer_path: Path

    @classmethod
    def load(cls, config_path: Path) -> "BatchConfig":
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return cls(**config)
