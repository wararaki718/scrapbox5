from bisect import bisect_left
from typing import Generator, List, Sequence


class BinarySearchSuggester:
    def __init__(self) -> None:
        self._index: List[str] = list()
    
    def index(self, suggestions: Sequence[str]) -> None:
        self._index.extend(suggestions)
        self._index.sort()
    
    def search(self, prefix: str) -> Generator[str, None, None]:
        position = bisect_left(self._index, prefix)

        for s in self._index[position:]:
            if s.startswith(prefix):
                yield s
            else:
                break
