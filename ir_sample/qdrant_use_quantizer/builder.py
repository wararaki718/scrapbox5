from typing import List

from qdrant_client.http.models import Filter, FieldCondition, MatchText, SearchParams, QuantizationSearchParams

from query import SearchQuery


class QueryBuilder:
    @classmethod
    def build(cls, key: str, text: str, vector: List[float], ef: int=128) -> SearchQuery:
        query_filter = Filter(
            must=[
                FieldCondition(
                    key=key,
                    match=MatchText(text=text)
                )
            ]
        )
        search_params = SearchParams(
            hnsw_ef=ef,
            exact=False,
            quantization=QuantizationSearchParams(
                ignore=False,
                rescore=False
            )
        )

        return SearchQuery(
            query_filter=query_filter,
            search_params=search_params,
            query_vector=vector
        )
