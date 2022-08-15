from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Item:
    name: str
    vector: List[float]
    price: float

    def __str__(self) -> str:
        return str(asdict(self)).replace("'", '"')
