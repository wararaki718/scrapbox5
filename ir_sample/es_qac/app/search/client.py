from typing import List, Optional

from elasticsearch import Elasticsearch


class ElasticsearchClient:
    def __init__(self, hosts: List[str]):
        self._client = Elasticsearch(hosts)
    
    def create_index(self, index_name: str, mapping: dict) -> dict:
        response = self._client.index(index=index_name, document=mapping)
        return response
    
    def bulk(self, items: List[dict]) -> dict:
        response = self._client.bulk(operations=items)
        return response

    def search(self, index_name: str, body: Optional[dict] = None) -> dict:
        response = self._client.search(index=index_name, body=body)
        return response
