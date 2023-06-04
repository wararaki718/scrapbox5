from typing import Optional

from qdrant_client.models import FieldCondition, MatchValue


class CategoryFilter:
    @classmethod
    def bulid(cls, category: Optional[str]) -> Optional[FieldCondition]:
        if category is None:
            return None
        
        return FieldCondition(
            key=category,
            match=MatchValue(value=category)
        )
