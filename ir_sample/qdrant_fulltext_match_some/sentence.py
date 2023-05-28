from dataclasses import dataclass, asdict


@dataclass
class Sentence:
    sentence_id: int
    sentence: str

    def to_dict(self) -> dict:
        return asdict(self)
