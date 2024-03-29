import logging
from pathlib import Path

from indexer import QdrantIndexer
from initializer import DataInitializer


logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(asctime)s %(module)s => %(message)s")
logger = logging.getLogger(__name__)


def main():
    initializer = DataInitializer()
    filepath = Path("data/Gift_Cards.json")
    store_path = Path("data/vector_cards.ndjson")
    initializer.initialize(filepath, store_path)

    indexer = QdrantIndexer()
    collection_name = "reviews"
    indexer.index(store_path, collection_name)

    logger.info("DONE")


if __name__ == "__main__":
    main()
