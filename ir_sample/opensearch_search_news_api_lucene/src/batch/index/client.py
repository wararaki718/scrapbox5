from dataclasses import asdict
from typing import List, Optional

from opensearchpy import OpenSearch

from schemas.config import ClientConfig
from schemas.news import News


class OpenSearchClient:
    def __init__(self, config: ClientConfig):
        self._client = OpenSearch(**asdict(config))
    
    def create_index(self, index_name: str, body: dict) -> dict:
        response = self._client.indices.create(index_name, body=body)
        return response
    
    def delete_index(self, index_name: str) -> dict:
        response = self._client.indices.delete(index=index_name)
        return response
    
    def bulk_insert(self, index_name: str, items: List[News]) -> dict:
        action = str({"index": { "_index": index_name}}).replace("'", '"')
        
        body = "\n".join(
            map(
                lambda item: f"{action}\n{item}",
                map(
                    lambda item: str(item), items
                )
            )
        )
        response = self._client.bulk(body=body, index=index_name)
        return response
    
    def search(self, index_name: str, body: Optional[dict]=None) -> dict:
        response = self._client.search(index=index_name, body=body)
        return response
