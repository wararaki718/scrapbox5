from typing import List

import numpy as np
from qdrant_client.models import ScoredPoint

from .builder import QueryBuilder
from .client import SearchClient


class QdrantSearch:
    def __init__(self):
        self._client = SearchClient()

    def search(self, collection_name: str) -> List[ScoredPoint]:
        key = "reviewText"
        value = "hello"
        vector = np.random.random(768).tolist()
        query = QueryBuilder.build(key, value, vector)

        response = self._client.search(collection_name=collection_name, query=query)
        return response
