from collections import defaultdict
from typing import Dict, Generator, List, Sequence

from .nlp import ngrams


class NGramSuggester:
    def __init__(self, ngram_size: int = 2) -> None:
        self._index: Dict[str, List[str]] = defaultdict(list)
        self._ngram_size = ngram_size
    
    def index(self, suggestions: Sequence[str]) -> None:
        for s in suggestions:
            tokens = ngrams(s, self._ngram_size)
            for token in tokens:
                self._index[token].append(s)

    def search(self, prefix: str, threshold: float = 0.9) -> Generator[str, None, None]:
        suggestions = defaultdict(int)
        tokens = list(ngrams(prefix, self._ngram_size))

        for token in tokens:
            for s in self._index.get(token, []):
                suggestions[s] += 1

        for s, n_grams in suggestions.items():
            rate = n_grams / len(tokens)
            if threshold < rate:
                yield s
