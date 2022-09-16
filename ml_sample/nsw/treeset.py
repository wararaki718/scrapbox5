import bisect
from typing import Generator, List, Optional, Set, Union

from node import NodeDistCloser


class TreeSet:
    def __init__(self, c: Optional[Union[list, set]]=None):
        self._treeset = list()
        if c is not None:
            self._add_all(c)
    
    def __getitem__(self, index: int) -> NodeDistCloser:
        return self._treeset[index]
    
    def __str__(self) -> str:
        return str(self._treeset)
    
    def __len__(self) -> int:
        return len(self._treeset)
    
    def __iter__(self) -> Generator[NodeDistCloser, None, None]:
        for item in self._treeset:
            yield item

    def add(self, e: Union[NodeDistCloser, "TreeSet"]) -> bool:
        if isinstance(e, list) or isinstance(e, set) or isinstance(e, TreeSet):
            return self._add_all(e)
        
        if e in self._treeset:
            return False

        bisect.insort(self._treeset, e)
        return True
    
    def first(self) -> NodeDistCloser:
        return self._treeset[0]
    
    def last(self) -> NodeDistCloser:
        return self._treeset[-1]
    
    def poll_first(self) -> NodeDistCloser:
        return self._treeset.pop(0)
    
    def poll_last(self) -> NodeDistCloser:
        return self._treeset.pop()
    
    def _add_all(self, e: Union[List[NodeDistCloser], Set[NodeDistCloser], "TreeSet"]) -> bool:
        is_added = False
        for item in e:
            if item in self._treeset:
                continue
            bisect.insort(self._treeset, item)
            is_added = True
        return is_added

    def remove(self, e: NodeDistCloser) -> bool:
        try:
            self._treeset.remove(e)
            return True
        except ValueError as e:
            return False

    def clear(self):
        self._treeset.clear()

    def is_empty(self) -> bool:
        return len(self._treeset) == 0

    def contains(self, e: NodeDistCloser) -> bool:
        return e in self._treeset

    def clone(self) -> "TreeSet":
        return TreeSet(self._treeset)
