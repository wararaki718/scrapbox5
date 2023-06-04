from typing import Optional, Union

from qdrant_client.models import FieldCondition, Filter, MatchText


class SentenceFilter:
    @classmethod
    def bulid(cls, text: Optional[str]) -> Optional[Union[FieldCondition, Filter]]:
        if text is None or len(text) == 0:
            return None
        
        tokens = text.split()
        if len(tokens) == 1:
            return FieldCondition(
                key="sentence",
                match=MatchText(text=tokens[0])
            )
        
        must = []
        for token in tokens:
            must.append(
                FieldCondition(
                    key="sentence",
                    match=MatchText(text=token)
                )
            )
        
        return Filter(must=must)
