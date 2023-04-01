import gc
import logging
from pathlib import Path

from config import ModelConfig
from dumper import GiftCardDumper
from iterator import TextIterator
from loader import GiftCardLoader
from postprocessor import GiftPostprocessor
from preprocessor import TextPreprocessor
from vectorizer import BertVectorizer


logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(asctime)s %(module)s => %(message)s")
logger = logging.getLogger(__name__)


def init_data():
    filepath = Path("data/Gift_Cards.json")
    loader = GiftCardLoader()
    cards = loader.load(filepath)
    logger.info(f"the number of cards: {len(cards)}")

    preprocessor = TextPreprocessor()
    texts = preprocessor.transform(cards)

    model_config = ModelConfig()
    iterator = TextIterator(texts)
    vectorizer = BertVectorizer(model_config)
    vectors = list()
    for chunk in iterator:
        vectors.extend(vectorizer.transform(chunk))
    logger.info(f"vectorized: ({len(vectors)}, {len(vectors[0])})") # dim=768

    postprocessor = GiftPostprocessor()
    vector_cards = postprocessor.transform(cards, vectors)
    del cards
    del vectors
    gc.collect()

    dumper = GiftCardDumper()
    dumppath = Path("data/vector_cards.ndjson")
    dumper.dump(vector_cards, dumppath)
    logger.info(f"save {dumppath}")
    del vector_cards
    gc.collect()


def main():
    init_data()
    logger.info("DONE")


if __name__ == "__main__":
    main()
