import pandas as pd

from .ages import AgesCategorizer


class TitanicPreprocessor:
    def __init__(self) -> None:
        self._ages_categorizer = AgesCategorizer()

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        keep_columns = ["Pclass", "Age", "Embarked"]
        df = df[keep_columns]
        df.dropna(inplace=True)

        df["Ages"] = self._ages_categorizer.transform(df["Age"])

        return df
