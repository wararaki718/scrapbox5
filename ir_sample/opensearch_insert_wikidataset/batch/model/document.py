from dataclasses import dataclass


@dataclass
class Document:
    text: str
    version_id: str
    wikidata_id: str
