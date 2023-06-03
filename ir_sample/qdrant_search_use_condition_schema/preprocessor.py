from typing import List

from qdrant_client.http.models import Batch, ExtendedPointId

from schema.sentence import Sentence


class BatchPreprocessor:
    def __init__(self):
        pass

    def transform(self, sentences: List[Sentence], vectors: List[List[float]]) -> Batch:
        ids: List[ExtendedPointId] = [
            sentence.sentence_id for sentence in sentences
        ]
        payloads = [
            sentence.to_dict() for sentence in sentences
        ]
        return Batch(
            ids=ids,
            payloads=payloads,
            vectors=vectors
        )
