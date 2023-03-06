from typing import Tuple

import numpy as np
import pandas as pd

from .components import AgesCategorizer


class TitanicPreprocessor:
    def __init__(self) -> None:
        self._ages_categorizer = AgesCategorizer()

    def transform(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, np.ndarray]:
        keep_columns = set(["Pclass", "Age", "Embarked", "Survived"])
        df.drop(labels=set(df.columns)-keep_columns, axis=1, inplace=True)
        df.dropna(inplace=True)

        df.loc[:,"Ages"] = self._ages_categorizer.transform(df["Age"])
        
        return df.drop("Survived", axis=1), df.Survived.values
