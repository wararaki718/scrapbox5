from typing import List

from qdrant_client.http.models import Filter, FieldCondition, MatchText, SearchParams, MatchValue, Range

from .components import CategoryFilter, CounterfactualFilter, PriceFilter, SentenceFilter
from schema.condition import Condition
from schema.query import SearchQuery


class QueryBuilder:
    @classmethod
    def build(cls, query: Condition, vector: List[float], ef: int=128) -> SearchQuery:
        conditions = [
            CategoryFilter.bulid(query.category),
            CounterfactualFilter.bulid(query.is_counterfactual),
            PriceFilter.bulid(query.price_lower, query.price_upper),
            SentenceFilter.bulid(query.key)
        ]
        must = list(filter(lambda x: x is not None, conditions))
        
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
