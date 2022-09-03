import bisect
from typing import Any, List, Optional, Set, Union


class TreeSet:
    def __init__(self, c: Optional[Union[list, set]]=None):
        self._treeset = list()
        if c is not None:
            self._add_all(c)
    
    def __str__(self) -> str:
        return str(self._treeset)
    
    def __len__(self) -> int:
        return len(self._treeset)

    def add(self, e: Any) -> bool:
        if isinstance(e, list) or isinstance(e, set):
            return self._add_all(e)
        
        if e in self._treeset:
            return False

        bisect.insort(self._treeset, e)
        return True
    
    def _add_all(self, e: Union[List[Any], Set[Any]]) -> bool:
        is_added = False
        for item in e:
            if item in self._treeset:
                continue
            bisect.insort(self._treeset, item)
            is_added = True
        return is_added

    def remove(self, e: Any) -> bool:
        try:
            self._treeset.remove(e)
            return True
        except ValueError as e:
            return False

    def clear(self):
        self._treeset.clear()

    def is_empty(self) -> bool:
        return len(self._treeset) == 0

    def contains(self, e: Any) -> bool:
        return e in self._treeset
