from typing import List, Tuple

import numpy as np
import pandas as pd


class PokemonPreprocessor:
    def __init__(self):
        pass

    def transform(self, df: pd.DataFrame) -> Tuple[List, np.ndarray]:
        names = df.Name.tolist()
        features = df.drop("Name", axis=1).values.astype(np.float32)

        return names, features
