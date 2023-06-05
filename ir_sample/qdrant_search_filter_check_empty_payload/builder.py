from typing import List

from qdrant_client.http.models import Filter, FieldCondition, MatchValue, SearchParams

from condition import SearchCondition
from query import SearchQuery


class QueryBuilder:
    @classmethod
    def build(cls, condition: SearchCondition, vector: List[float], ef: int=128) -> SearchQuery:
        must=[]
        if condition.city is not None:
            must.append(
                FieldCondition(
                    key="city",
                    match=MatchValue(value=condition.city)
                )
            )

        if condition.color is not None:
            must.append(
                FieldCondition(
                    key="color",
                    match=MatchValue(value=condition.color)
                )
            )

        if len(must) > 0:
            query_filter = Filter(
                must=must
            )
        else:
            query_filter = None

        search_params = SearchParams(
            hnsw_ef=ef,
            exact=False
        )

        return SearchQuery(
            query_filter=query_filter,
            search_params=search_params,
            query_vector=vector
        )
