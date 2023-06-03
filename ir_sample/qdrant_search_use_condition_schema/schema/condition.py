from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Condition:
    key: Optional[str] = None
    category: Optional[str] = None
    price_upper: Optional[int] = None
    price_lower: Optional[int] = None
    is_counterfactual: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)

    def is_empty(self) -> bool:
        return self.key is None and self.category is None and self.price_lower is None and self.price_upper is None and self.is_counterfactual is None
