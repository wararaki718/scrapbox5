from dataclasses import dataclass, asdict
from typing import List, Optional

from qdrant_client.http.models import Filter, SearchParams


@dataclass
class SearchQuery:
    query_filter: Optional[Filter] = None
    search_params: Optional[SearchParams] = None
    query_vector: Optional[List[float]] = None

    def to_dict(self) -> dict:
        return asdict(self)
