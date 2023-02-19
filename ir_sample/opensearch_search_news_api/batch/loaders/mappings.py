import json
from pathlib import Path


class MappingsLoader:
    @classmethod
    def load(cls, mappings_path: Path) -> dict:
        with open(mappings_path) as f:
            mappings = json.load(f)
        return mappings
