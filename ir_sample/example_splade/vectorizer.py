from functools import partial
from typing import Dict, List

import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer


class DocumentTransformer:
    def __init__(self, model_name: str) -> None:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._vocabs = tokenizer.get_vocab().items()
        self._tokenize = partial(tokenizer, return_tensors="pt")
        self._model = AutoModelForMaskedLM.from_pretrained(model_name)
    
    def transform(self, texts: List[str]) -> torch.Tensor:
        tokens = self._tokenize(texts)
        output = self._model(**tokens)
        vectors = torch.max(
            torch.log(1 + torch.relu(output.logits)) * tokens.attention_mask.unsqueeze(-1),
            dim=1
        )[0].squeeze()
        return vectors
    
    def get_vocabs(self) -> Dict[str, int]:
        return self._vocabs


class QueryTransformer:
    def __init__(self, model_name: str) -> None:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._tokenize = partial(tokenizer, return_tensors="pt", padding=True, truncation=True)
        self._model = AutoModelForMaskedLM.from_pretrained(model_name)
    
    def transform(self, texts: List[str]) -> torch.Tensor:
        tokens = self._tokenize(texts)
        output = self._model(**tokens)
        vectors = torch.max(
            torch.log(1 + torch.relu(output.logits)) * tokens.attention_mask.unsqueeze(-1),
            dim=1
        )[0].squeeze()
        return vectors
