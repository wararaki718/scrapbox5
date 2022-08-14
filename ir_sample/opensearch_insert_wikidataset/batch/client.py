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
        response = self._client.index(index=index_name, body=body, refresh=True)
        return response
    
    def bulk_insert(self, index_name: str, documents: List[Document], chunksize: int=128) -> dict:
        action = str({"index": { "_index": index_name}}).replace("'", '"')
        
        for i in range(0, len(documents), chunksize):
            body = "\n".join(
                map(
                    lambda document: f"{action}\n{document}",
                    map(
                        lambda document: str(document),
                        documents[i:i+chunksize]
                    )
                )
            )
            response = self._client.bulk(body=body, index=index_name)
        return response

    def search(self, index_name: str, body: Optional[dict]=None) -> dict:
        response = self._client.search(index=index_name, body=body)
        return response

    def train(self, model_name: str, body: dict) -> dict:
        train_path = f"/_plugins/_knn/models/{model_name}/_train"
        response = self._client.transport.perform_request(
            "POST",
            train_path,
            body=body
        )
        return response

    def get_model_status(self, model_name: str) -> dict:
        response = self._client.transport.perform_request(
            "GET",
            f"/_plugins/_knn/models/{model_name}"
        )
        return response

    def delete_model(self, model_name: str) -> dict:
        response = self._client.transport.perform_request(
            "DELETE",
            f"/_plugins/_knn/models/{model_name}"
        )
        return response
