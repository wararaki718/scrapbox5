from functools import partial
from typing import List

from .client import OpenSearchClient
from .postprocesser import Postprocessor
from .query import QueryBuilder
from .vectorizer import BertVectorizer
from api.schemas.config import ClientConfig, ModelConfig, SearchConfig
from api.schemas.response import News


class VectorSearch:
    def __init__(self,
                 client_config: ClientConfig,
                 model_config: ModelConfig,
                 search_config: SearchConfig):
        self._index_name = search_config.index_name
        self._client = OpenSearchClient(client_config)
        self._vectorizer = BertVectorizer(model_config)
        self._postprocessor = Postprocessor()

    def search(self, context: str) -> List[News]:
        vector = self._vectorizer.transform(context)
        query = QueryBuilder.build(vector)
        response = self._client.search(self._index_name, query)
        results = self._postprocessor.transform(response["hits"]["hits"])
        return results
