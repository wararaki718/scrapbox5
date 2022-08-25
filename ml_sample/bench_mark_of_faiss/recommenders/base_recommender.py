from typing import Any


class BaseRecommender:
    def __init__(self, *args: Any):
        pass

    def add(self, *args: Any):
        pass
    
    def search(self, *args: Any) -> tuple:
        pass
