from typing import Dict, List


class InvertedIndex:
    def __init__(self, index: Dict[str, List[int]]):
        self._index = index

    def __getitem__(self, key: str) -> List[int]:
        return self._index[key]
    
    def get(self, key: str, default: List[int] = []) -> List[int]:
        return self._index.get(key, default)
