from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict


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
