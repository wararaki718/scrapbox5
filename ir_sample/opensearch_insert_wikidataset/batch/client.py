from dataclasses import asdict
from typing import List, Optional

from opensearchpy import OpenSearch

from config import ClientConfig
from model import Document


class OpenSearchClient:
    def __init__(self, config: ClientConfig):
        self._client = OpenSearch(**asdict(config))
    
    def create_index(self, index_name: str, body: dict) -> dict:
        response = self._client.indices.create(index_name, body=body)
        return response
    
    def delete_index(self, index_name: str) -> dict:
        response = self._client.indices.delete(index = index_name)
        return response
    
    def insert(self, index_name: str, document: Document) -> dict:
        body = asdict(document)
        response = self._client.index(index = index_name, body = body, refresh = True)
        return response
    
    def bulk_insert(self, index_name: str, documents: List[Document]) -> dict:
        action = str({"index": { "_index": index_name}})
        body = "\n".join(
            map(
                lambda document: f"{action}\n{document}".replace("'", '"'),
                map(
                    lambda document: str(asdict(document)),
                    documents
                )
            )
        )
        response = self._client.bulk(body=body, index=index_name)
        return response

    def search(self, index_name: str, body: Optional[dict]=None) -> dict:
        response = self._client.search(index=index_name, body=body)
        return response
