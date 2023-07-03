from functools import partial

from transformers import AutoTokenizer


class CustomTokenizer:
    def __init__(self, model_name: str, max_length: int=128) -> None:
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._tokenize = partial(
            self._tokenizer,
            add_special_tokens=True,
            padding="longest",
            truncation="longest_first",
            max_length=max_length,
            return_attention_mask=True
        )
    
    def tokenize(self, text: str) -> dict:
        return self._tokenize(text)

    def get_tokens_map(self) -> dict:
        return self._tokenizer.special_tokens_map
    
    def get_vocabs(self) -> dict:
        return self._tokenizer.vocab
