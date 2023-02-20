from functools import partial
from typing import List

from transformers import AutoModel, AutoTokenizer

from schemas.news import News
from schemas.config import ModelConfig
from .utils import try_gpu


class BertVectorizer:
    def __init__(self, config: ModelConfig):
        self._encoder = partial(
            AutoTokenizer.from_pretrained(config.name).batch_encode_plus,
            **config.params()
        )
        self._model = try_gpu(AutoModel.from_pretrained(config.name))
    
    def transform(self, news: List[News], batch_size: int = 32) -> List[List[float]]:
        vectors = []
        for i in range(0, len(news), batch_size):
            tokens = self._encoder(map(lambda x: x.context, news[i:i+batch_size]))
            out = self._model(
                input_ids = try_gpu(tokens["input_ids"]),
                attention_mask = try_gpu(tokens["attention_mask"])
            )
            vector = out.last_hidden_state.mean(1).detach().cpu().numpy().tolist()
            vectors.extend(vector)
        return vectors
