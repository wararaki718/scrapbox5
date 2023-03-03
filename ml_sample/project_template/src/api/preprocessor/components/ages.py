import pandas as pd


class AgesCategorizer:
    def __init__(self) -> None:
        pass

    def transform(self, age: int) -> int:
        return int(age/10)*10
