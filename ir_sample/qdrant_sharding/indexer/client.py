from qdrant_client import QdrantClient
from qdrant_client.http.models import Batch, SnapshotDescription, UpdateResult, VectorParams


class SearchClient:
    def __init__(self, host: str="localhost", port: int=6333):
        self._client = QdrantClient(host=host, port=port, timeout=300)

    def create_index(self, collection_name: str, params: VectorParams, n_shards: int=8) -> bool:
        self._client.recreate_collection(
            collection_name=collection_name,
            vectors_config=params,
            shard_number=n_shards
        )
    
    def insert(self, collection_name: str, points: Batch) -> UpdateResult:
        response = self._client.upsert(
            collection_name=collection_name,
            points=points
        )
        return response

    def create_snapshot(self, collection_name: str) -> SnapshotDescription:
        response = self._client.create_snapshot(collection_name=collection_name)
        return response
