from functools import partial
from typing import List

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class QueryGenerator:
    def __init__(self, model_name: str) -> None:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._encode = partial(
            tokenizer.encode,
            return_tensors="pt"
        )
        self._generate = partial(
            AutoModelForSeq2SeqLM.from_pretrained(model_name).generate,
            max_length=64,
            do_sample=True,
            top_p=0.95,
            top_k=10,
            num_return_sequences=5
        )
        self._decode = partial(
            tokenizer.decode,
            skip_special_tokens=True
        )
    
    def generate(self, text: str) -> List[str]:
        input_ids = self._encode(text)
        with torch.no_grad():
            outputs = self._generate(input_ids=input_ids)
        queries = [self._decode(output) for output in outputs]

        return queries
