import logging
from pathlib import Path
from time import sleep

from qdrant_client.models import Distance, VectorParams

from .client import SearchClient
from .iterator import BatchIterator
from .loader import CardLoader


logger = logging.getLogger(__name__)


class QdrantIndexer:
    def __init__(self, host: str="127.0.0.1", port: int=6333):
        self._loader = CardLoader()
        self._client = SearchClient(host=host, port=port)

    def index(self, filepath: Path, collection_name: str, batch_size: int=1024):
        cards = self._loader.load(filepath)
        logger.info(f"loaded cards: {len(cards)}")

        params = VectorParams(
            size=len(cards[0].vector),
            distance=Distance.COSINE
        )
        self._client.create_index(collection_name, params)
        logger.info(f"{collection_name} is created!")

        iterator = BatchIterator(cards, batch_size)
        for points in iterator:
            self._client.insert(collection_name, points)
            logger.info(f"insert data: {len(points.ids)}")
        sleep(3)

        logger.info("create snapshot:")
        snapshot = self._client.create_snapshot(collection_name)
        sleep(3)
        logger.info(f"{snapshot.name} is created.")
