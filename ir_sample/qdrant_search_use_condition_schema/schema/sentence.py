from dataclasses import dataclass, asdict


@dataclass
class Sentence:
    sentence_id: int
    sentence: str
    category: str
    price: int
    is_counterfactual: int

    def to_dict(self) -> dict:
        return asdict(self)
