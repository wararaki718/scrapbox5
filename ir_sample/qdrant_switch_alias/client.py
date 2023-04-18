from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http.models import Batch, ScoredPoint, UpdateResult, VectorParams, CreateAliasOperation, CreateAlias, DeleteAlias, DeleteAliasOperation

from query import SearchQuery


class SearchClient:
    def __init__(self, host: str="localhost", port: int=6333, grpc_port: int=6334, prefer_grpc: bool=True):
        self._client = QdrantClient(
            host=host,
            port=port,
            grpc_port=grpc_port,
            prefer_grpc=prefer_grpc
        )

    def create_index(self, collection_name: str, params: VectorParams) -> bool:
        response = self._client.recreate_collection(
            collection_name=collection_name,
            vectors_config=params
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

    def update_alias(self, collection_name: str, alias_name: str) -> bool:
        alias = CreateAlias(
            collection_name=collection_name,
            alias_name=alias_name
        )
        response = self._client.update_collection_aliases(
            change_aliases_operations=[
                CreateAliasOperation(
                    create_alias=alias
                )
            ]
        )
        return response

    def delete_alias(self, alias_name: str) -> bool:
        alias = DeleteAlias(
            alias_name=alias_name
        )
        response = self._client.update_collection_aliases(
            change_aliases_operations=[
                DeleteAliasOperation(
                    delete_alias=alias
                )
            ]
        )
        return response

    def switch_alias(self, collection_name: str, alias_name: str) -> bool:
        delete_alias = DeleteAlias(
            alias_name=alias_name
        )
        create_alias = CreateAlias(
            alias_name=alias_name,
            collection_name=collection_name
        )

        response = self._client.update_collection_aliases(
            change_aliases_operations=[
                DeleteAliasOperation(
                    delete_alias=delete_alias
                ),
                CreateAliasOperation(
                    create_alias=create_alias
                )
            ]
        )
        return response
