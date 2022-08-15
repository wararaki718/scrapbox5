from dataclasses import asdict, dataclass


@dataclass
class News:
    newsid: str
    context: str
    isfake: int
    nchar_real: int
    nchar_fake: int

    def __str__(self) -> str:
        return str(asdict(self)).replace("'", '"')
