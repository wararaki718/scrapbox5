from typing import List

from qdrant_client.http.models import Filter, FieldCondition, MatchValue, SearchParams

from condition import SearchCondition
from query import SearchQuery


class QueryBuilder:
    @classmethod
    def build(cls, condition: SearchCondition, vector: List[float], ef: int=128) -> SearchQuery:
        query_filter = Filter(
            must=[
                FieldCondition(
                    key=condition.key,
                    match=MatchValue(value=condition.value)
                )
            ]
        )
        search_params = SearchParams(
            hnsw_ef=ef,
            exact=False
        )

        return SearchQuery(
            query_filter=query_filter,
            search_params=search_params,
            query_vector=vector
        )
