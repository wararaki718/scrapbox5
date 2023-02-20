from dataclasses import asdict, dataclass, field
from typing import List


@dataclass
class News:
    newsid: str
    context: str
    isfake: int
    nchar_real: int
    nchar_fake: int
    vector: List[float] = field(
        default_factory=lambda: []
    )

    def __str__(self) -> str:
        return str(asdict(self)).replace("'", '"')
