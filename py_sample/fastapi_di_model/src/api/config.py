from pathlib import Path

import yaml
from pydantic import BaseModel


class Config(BaseModel):
    threshold: int

    @classmethod
    def load(cls, config_path: Path) -> "Config":
        with open(config_path) as f:
            config = yaml.safe_load(f)
        
        return cls(**config)
