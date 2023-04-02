from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class GiftCardWithVector:
    overall: int
    verified: bool
    reviewTime: str
    reviewerID: str
    asin: str
    unixReviewTime: int
    vector: List[float]
    reviewerName: Optional[str] = None
    summary: Optional[str] = None
    reviewText: Optional[str] = None
    image: Optional[List[str]] = None
    style: Optional[dict] = None
    vote: Optional[str] = None

    def dict(self) -> dict:
        return asdict(self)
