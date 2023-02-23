import json
from pathlib import Path
from typing import List


class BulkLoader:
    def __init__(self) -> None:
        pass

    @classmethod
    def load(cls, filename: Path) -> List[dict]:
        items = []
        with open(filename) as f:
            for line in f:
                item = json.loads(line)
                items.append(item)
        return items
