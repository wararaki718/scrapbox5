import json
from pathlib import Path


class MappingLoader:
    def __init__(self) -> None:
        pass

    @classmethod
    def load(cls, filename: Path) -> dict:
        with open(filename) as f:
            mapping = json.load(f)
        return mapping
