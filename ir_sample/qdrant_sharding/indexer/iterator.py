import uuid
from typing import Generator, List

from qdrant_client.http.models import Batch

from .card import GiftCardWithVector


class BatchIterator:
    def __init__(self, cards: List[GiftCardWithVector], batch_size: int = 1024):
        self._cards = cards
        self._batch_size = batch_size
    
    def __iter__(self) -> Generator[Batch, None, None]:
        ids = []
        payloads = []
        vectors = []
        for card in self._cards:
            payload = card.dict()
            del payload["vector"]

            ids.append(uuid.uuid4())
            vectors.append(card.vector)
            payloads.append(payload)
            if len(ids) < self._batch_size:
                yield Batch(
                    ids=ids,
                    payloads=payloads,
                    vectors=vectors
                )
                ids = []
                vectors = []
                payloads = []
        
        if len(ids) > 0:
            yield Batch(
                ids=ids,
                payloads=payloads,
                vectors=vectors
            )
