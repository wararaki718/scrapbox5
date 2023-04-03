from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http.models import ScoredPoint

from .query import SearchQuery


class SearchClient:
    def __init__(self, host: str="localhost", port: int=6333):
        self._client = QdrantClient(host=host, port=port)

    def search(self, collection_name: str, query: SearchQuery) -> List[ScoredPoint]:
        response = self._client.search(
            collection_name=collection_name,
            **query.to_dict(),
            limit=10
        )
        return response
