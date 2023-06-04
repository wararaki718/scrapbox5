from typing import Optional

from qdrant_client.models import FieldCondition, Range


class PriceFilter:
    @classmethod
    def bulid(cls, price_lower: Optional[int], price_upper: Optional[int]) -> Optional[FieldCondition]:
        if price_lower is None and price_upper is None:
            return None
        
        return FieldCondition(
            key="price",
            range=Range(
                gte=price_lower,
                lte=price_upper
            )
        )
