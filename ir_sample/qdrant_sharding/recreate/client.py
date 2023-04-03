from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http.models import CollectionInfo, InitFrom, VectorParams


class SearchClient:
    def __init__(self, host: str="localhost", port: int=6333):
        self._client = QdrantClient(host=host, port=port)

    def recreate_index(self, collection_name: str, params: VectorParams, base: str, n_shards: int=8) -> bool:
        response = self._client.recreate_collection(
            collection_name=collection_name,
            vectors_config=params,
            init_from=InitFrom(collection=base),
            shard_number=n_shards
        )
        return response
    
    def get_cluster(self, collection_name: str) -> CollectionInfo:
        response = self._client.get_collection(collection_name)
        return response
