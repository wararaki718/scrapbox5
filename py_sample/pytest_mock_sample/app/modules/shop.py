from typing import List

from .item import Item


class Shop:
    _shelf: List[Item]

    def __init__(self):
        self._shelf = []

    def set_item(self, item: Item):
        self._shelf.append(item)
    
    def get_item(self, index: int) -> Item:
        return self._shelf[index]
