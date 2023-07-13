from functools import partial
from typing import List, Tuple

import torch
from splade.models.transformer_rep import Splade
from transformers import AutoTokenizer


class DocumentVectorizer:
    def __init__(self, model: Splade, tokenizer: AutoTokenizer) -> None:
        self._model = model
        self._tokenize = partial(
            tokenizer,
            padding=True,
            truncation=True,
            return_tensors="pt",
            max_length=500
        )

    def vectorize(self, texts: torch.Tensor) -> Tuple[List[float], List[float], List[float]]:
        self._model.eval()
        with torch.no_grad():
            tokens: torch.Tensor = self._tokenize(texts)
            embeddings = self._model(d_kwargs=tokens)
        rows, columns = torch.nonzero(embeddings["d_rep"], as_tuple=True)
        values = embeddings["d_rep"][rows, columns].tolist()

        return rows.tolist(), columns.tolist(), values
