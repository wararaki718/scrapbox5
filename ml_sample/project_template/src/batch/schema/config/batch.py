from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class BatchConfig:
    titanic_path: Path

    def __post_init__(self):
        self.titanic_path = Path(self.titanic_path)

    @classmethod
    def load(cls, config_path: Path) -> "BatchConfig":
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return cls(**config)
