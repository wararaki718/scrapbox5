from typing import Callable, Generator, List, Sequence

from .distance import longest_common_substring, levenshtein_distance, hamming_distance


class EditDistanceSuggester:
    _edit_distance: Callable[[str, str], int]

    def __init__(self, mode: str="levenshtein") -> None:
        self._index: List[str] = list()

        if mode == "lcs":
            self._edit_distance = longest_common_substring
        elif mode == "levenshtein":
            self._edit_distance = levenshtein_distance
        elif mode == "hamming":
            self._edit_distance = hamming_distance
        else:
            raise NotImplementedError
    
    def index(self, suggestions: Sequence[str]) -> None:
        self._index.extend(suggestions)
    
    def search(self, prefix: str, threshold: int=1) -> Generator[str, None, None]:
        for s in self._index:
            distance = self._edit_distance(prefix, s[:len(prefix)])
            if distance <= threshold:
                yield s
