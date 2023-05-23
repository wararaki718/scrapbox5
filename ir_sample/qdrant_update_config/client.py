from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http.models import Batch, ScoredPoint, UpdateResult, VectorParams, OptimizersConfigDiff, CollectionInfo

from query import SearchQuery


class SearchClient:
    def __init__(self, host: str="localhost", port: int=6333):
        self._client = QdrantClient(host=host, port=port)

    def create_index(self, collection_name: str, vector_config: VectorParams) -> bool:
        response = self._client.recreate_collection(
            collection_name=collection_name,
            vectors_config=vector_config,
            on_disk_payload=False
        )
        return response
    
    def insert(self, collection_name: str, points: Batch) -> UpdateResult:
        response = self._client.upsert(
            collection_name=collection_name,
            points=points
        )
        return response

    def search(self, collection_name: str, query: SearchQuery) -> List[ScoredPoint]:
        response = self._client.search(
            collection_name=collection_name,
            **query.to_dict()
        )
        return response

    def delete_index(self, collection_name: str) -> bool:
        response = self._client.delete_collection(collection_name=collection_name)
        return response

    def update_collection(self, collection_name: str, optimizer_config: OptimizersConfigDiff) -> bool:
        # dynamic paramter only
        response = self._client.update_collection(
            collection_name=collection_name,
            optimizer_config=optimizer_config
        )
        return response

    def get_collection(self, collection_name: str) -> CollectionInfo:
        response = self._client.get_collection(collection_name=collection_name)
        return response