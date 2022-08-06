from dataclasses import asdict

from opensearchpy import OpenSearch

from config import ClientConfig


class OpenSearchClient:
    def __init__(self, config: ClientConfig):
        self._client = OpenSearch(**asdict(config))
    
    def create_index(self, index_name: str, body: dict) -> dict:
        response = self._client.indices.create(index_name, body=body)
        return response
    
    def delete_index(self, index_name: str) -> dict:
        response = self._client.indices.delete(index = index_name)
        return response
    
    #def insert(self, )

    def search(self, index_name: str, body: dict) -> dict:
        response = self._client.search(index=index_name, body=body)
        return response
    
