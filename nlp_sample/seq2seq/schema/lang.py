from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List

import torch

from .enum import TOKEN


@dataclass
class Lang:
    name: str
    word2index: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    word2count: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    index2word: Dict[int, str] = field(default_factory=lambda: {0: "SOS", 1: "EOS"})
    n_words: int = 2

    def add(self, sentence: str) -> None:
        for word in sentence.split(" "):
            if word not in self.word2index:
                self.word2index[word] = self.n_words
                self.index2word[self.n_words] = word
                self.n_words += 1
            self.word2count[word] += 1

    def get_ids(self, sentence: str) -> List[int]:
        return [self.word2index[word] for word in sentence.split(" ")]

    def get_tensor(self, sentence: str) -> torch.Tensor:
        ids = self.get_ids(sentence)
        ids.append(TOKEN.EOS)
        return torch.Tensor(ids).long().view(1, -1)
