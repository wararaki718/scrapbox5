from dataclasses import dataclass, asdict
from typing import List

from qdrant_client.http.models import Filter, SearchParams


@dataclass
class SearchQuery:
    query_filter: Filter
    search_params: SearchParams
    query_vector: List[float]

    def to_dict(self) -> dict:
        return asdict(self)
