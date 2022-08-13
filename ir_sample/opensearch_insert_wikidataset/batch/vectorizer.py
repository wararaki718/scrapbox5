from functools import partial
from typing import List

import numpy as np
from sklearn.decomposition import PCA
from transformers import AutoModel, AutoTokenizer

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
        self._pca = PCA(n_components=4)
    
    def fit_transform(self, texts: List[str], batch_size: int = 16) -> List[List[float]]:
        vectors = []
        for i in range(0, len(texts), batch_size):
            tokens = self._encoder(texts[i:i+batch_size])
            out = self._model(
                input_ids = try_gpu(tokens["input_ids"]),
                attention_mask = try_gpu(tokens["attention_mask"])
            )
            vector = out.last_hidden_state.mean(1).detach().cpu().numpy().tolist()
            vectors.extend(vector)
        return self._pca.fit_transform(np.array(vectors)).tolist()
