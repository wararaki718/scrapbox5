from typing import Optional

from qdrant_client.models import FieldCondition, MatchValue


class CounterfactualFilter:
    @classmethod
    def bulid(cls, counterfactual: Optional[int]) -> Optional[FieldCondition]:
        if counterfactual is None:
            return None
        
        return FieldCondition(
            key="is_counterfactual",
            match=MatchValue(value=counterfactual)
        )
