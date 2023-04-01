import gc
import logging
from pathlib import Path

from .config import ModelConfig
from .dumper import GiftCardDumper
from .iterator import TextIterator
from .loader import GiftCardLoader
from .postprocessor import GiftPostprocessor
from .preprocessor import TextPreprocessor
from .vectorizer import BertVectorizer


logger = logging.getLogger(__name__)


class DataInitializer:
    def __init__(self, model_config: ModelConfig = ModelConfig()):
        self._loader = GiftCardLoader()
        self._preprocessor = TextPreprocessor()
        self._vectorizer = BertVectorizer(model_config)
        self._postprocessor = GiftPostprocessor()
        self._dumper = GiftCardDumper()

    def initialize(self, filepath: Path, store_path: Path):
        if store_path.exists():
            logger.info("{store_path} is already existed. skip initialization.")
            return

        cards = self._loader.load(filepath)
        logger.info(f"the number of cards: {len(cards)}")
        
        texts = self._preprocessor.transform(cards)
        logger.info(f"preprocessed.")
        
        vectors = list()
        iterator = TextIterator(texts)
        for chunk in iterator:
            vectors.extend(self._vectorizer.transform(chunk))
        logger.info(f"vectorized: ({len(vectors)}, {len(vectors[0])})") # dim=768

        vector_cards = self._postprocessor.transform(cards, vectors)
        del cards
        del vectors
        gc.collect()

        self._dumper.dump(vector_cards, store_path)
        logger.info(f"save {store_path}")
        del vector_cards
        gc.collect()
