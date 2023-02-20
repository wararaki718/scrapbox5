from functools import partial
from typing import List

from transformers import AutoModel, AutoTokenizer

from api.schemas.config import ModelConfig
from .utils import try_gpu


class BertVectorizer:
    def __init__(self, config: ModelConfig):
        self._encoder = partial(
            AutoTokenizer.from_pretrained(config.name).batch_encode_plus,
            **config.params()
        )
        self._model = try_gpu(AutoModel.from_pretrained(config.name))
    
    def transform(self, context: str) -> List[float]:
        tokens = self._encoder([context])
        out = self._model(
            input_ids = try_gpu(tokens["input_ids"]),
            attention_mask = try_gpu(tokens["attention_mask"])
        )
        vectors = out.last_hidden_state.mean(1).detach().cpu().numpy().tolist()
        return vectors[0]
