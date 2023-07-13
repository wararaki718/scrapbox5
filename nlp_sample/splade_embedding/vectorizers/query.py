from functools import partial
from typing import List, Tuple

import torch
from splade.models.transformer_rep import Splade
from transformers import AutoTokenizer


class QueryVectorizer:
    def __init__(self, model: Splade, tokenizer: AutoTokenizer) -> None:
        self._model = model
        self._tokenize = partial(
            tokenizer,
            padding=True,
            truncation=True,
            return_tensors="pt",
            max_length=500
        )

    def vectorize(self, queries: torch.Tensor) -> Tuple[List[torch.Tensor], List[float]]:
        self._model.eval()
        with torch.no_grad():
            tokens: torch.Tensor = self._tokenize(queries)
            embeddings = self._model(q_kwargs=tokens)
        rows, columns = torch.nonzero(embeddings["q_rep"], as_tuple=True)
        values = embeddings["q_rep"][rows, columns].tolist()

        return columns.tolist(), values
