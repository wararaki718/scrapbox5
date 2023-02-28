import pandas as pd


class AgesCategorizer:
    def __init__(self) -> None:
        pass

    def transform(self, ages: pd.Series) -> pd.Series:
        return ages.apply(lambda age: int(age/10)*10 if age == age else age)
