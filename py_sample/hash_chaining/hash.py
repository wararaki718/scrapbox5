from typing import List


class Hash:
    def __init__(self, n_tables: int):
        self._n_tables = n_tables
        self._table = [[] for _ in range(n_tables)]
    
    def insert(self, key: int):
        index = self._hashing(key)
        self._table[index].append(key)

    def delete(self, key: int):
        index = self._hashing(key)
        for i, elem in enumerate(self._table[index]):
            if key == elem:
                del self._table[index][i]
                return

    def _hashing(self, item: int) -> int:
        return (item % self._n_tables)

    def get_table(self) -> List[List[int]]:
        return self._table
    
    def __iter__(self) -> List[int]:
        for row in self._table:
            yield row
