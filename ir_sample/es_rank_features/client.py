from typing import List, Optional

from elasticsearch import Elasticsearch

from schema.doc import Document


class ElasticsearchClient:
    def __init__(self, hosts: List[str], timeout: float=60.0):
        self._client = Elasticsearch(hosts, timeout=timeout)
    
    def create_index(self, index_name: str, mappings: dict) -> dict:
        response = self._client.indices.create(index=index_name, body=mappings)
        return response
    
    def insert(self, index_name: str, id_: int, doc: Document) -> dict:
        response = self._client.create(index=index_name, id=id_, body=doc.dict())
        return response

    def search(self, index_name: str, body: Optional[dict] = None) -> dict:
        response = self._client.search(index=index_name, body=body)
        return response

    def count(self, index_name: str) -> dict:
        response = self._client.count(index=index_name)
        return response

    def delete_index(self, index_name: str) -> dict:
        response = self._client.indices.delete(index=index_name)
        return response
