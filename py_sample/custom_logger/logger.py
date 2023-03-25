import logging
import logging.config
from pathlib import Path
from typing import Optional

import yaml


# singleton
class CustomLogger:
    logger: Optional[logging.Logger] = None

    @classmethod
    def instance(cls, name: str, config_path: Path) -> logging.Logger:
        if cls.logger is not None:
            return cls.logger

        with open(config_path) as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
        cls.logger = logging.getLogger(name)

        return cls.logger
