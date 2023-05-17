from dataclasses import dataclass, asdict


@dataclass
class Sentence:
    sentence_id: int
    sentence: str
    is_counterfactual: int

    def to_dict(self) -> dict:
        return asdict(self)
