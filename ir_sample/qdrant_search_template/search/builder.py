from typing import List

from qdrant_client.http.models import Filter, FieldCondition, MatchText, SearchParams, MatchValue, Range

from schema.condition import Condition
from schema.query import SearchQuery


class QueryBuilder:
    @classmethod
    def build(cls, condition: Condition, vector: List[float], ef: int=128) -> SearchQuery:
        must = []
        if condition.key is not None:
            must.append(
                FieldCondition(
                    key="sentence",
                    match=MatchText(text=condition.key)
                )
            )
        
        if condition.category is not None:
            must.append(
                FieldCondition(
                    key="category",
                    match=MatchValue(value=condition.category)
                )
            )
        
        if condition.price_lower is not None and condition.price_upper is not None:
            must.append(
                FieldCondition(
                    key="price",
                    range=Range(
                        gte=condition.price_lower,
                        lte=condition.price_upper
                    )
                )
            )
        
        if condition.is_counterfactual is not None:
            must.append(
                FieldCondition(
                    key="is_counterfactual",
                    match=MatchValue(value=condition.is_counterfactual)
                )
            )

        query_filter = Filter(must=must)
        search_params = SearchParams(
            hnsw_ef=ef,
            exact=False
        )

        return SearchQuery(
            query_filter=query_filter,
            search_params=search_params,
            query_vector=vector
        )
