from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Document:
    topics: Dict[str, float]
    negative_reviews: Dict[str, float]
    
    def dict(self) -> dict:
        return asdict(self)
