from collections import defaultdict
from typing import Dict, Generator, List, Sequence


class EdgeNGramSuggester:
    def __init__(self) -> None:
        self._index: Dict[str, List[str]] = defaultdict(list)
    
    def index(self, suggestions: Sequence[str]) -> None:
        for s in suggestions:
            for i, _ in enumerate(s, start=1):
                ngram = s[:i]
                self._index[ngram].append(s)

    def search(self, prefix: str) -> Generator[str, None, None]:
        suggestions = self._index.get(prefix, [])
        for s in suggestions:
            yield s
