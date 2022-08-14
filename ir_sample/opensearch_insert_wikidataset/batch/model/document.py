from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Document:
    text: str
    version_id: str
    wikidata_id: str
    vector: List[float]

    def __str__(self) -> str:
        return str(asdict(self)).replace("'", '"')
