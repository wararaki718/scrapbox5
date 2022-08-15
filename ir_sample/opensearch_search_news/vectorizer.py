from functools import partial
from typing import List

from transformers import AutoModel, AutoTokenizer

from news import News
from utils import try_gpu


class BertVectorizer:
    def __init__(self, model_name: str):
        self._encoder = partial(
            AutoTokenizer.from_pretrained(model_name).batch_encode_plus,
            **{
                "truncation": True,
                "add_special_tokens": True,
                "max_length": 128,
                "padding": "max_length",
                "return_tensors": "pt"
            }
        )
        self._model = try_gpu(AutoModel.from_pretrained(model_name))
    
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
