from typing import Generator, List, Sequence


class BruteForceSuggester:
    def __init__(self) -> None:
        self._index: List[str] = list()
    
    def index(self, suggestions: Sequence[str]) -> None:
        self._index.extend(suggestions)
    
    def search(self, prefix: str) -> Generator[str, None, None]:
        for s in self._index:
            if s.startswith(prefix):
                yield s
