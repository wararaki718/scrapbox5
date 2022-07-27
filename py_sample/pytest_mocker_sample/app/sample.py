import os


def set_value() -> int:
    return 1


class Sample:
    _field: int = 3000
    def __init__(self):
        self._value = set_value()
        self._items = os.listdir(".")
    
    def method(self) -> int:
        return 1000
