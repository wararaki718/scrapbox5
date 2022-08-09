from dataclasses import dataclass
from typing import List


@dataclass
class Document:
    text: str
    version_id: str
    wikidata_id: str
    vector: List[int]
