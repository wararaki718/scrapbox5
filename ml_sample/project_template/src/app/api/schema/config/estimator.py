from pathlib import Path

from pydantic import BaseModel


class EstimatorConfig(BaseModel):
    model_path: Path
