from pathlib import Path

from pydantic import BaseModel


class VectorizerConfig(BaseModel):
    vectorizer_path: Path
