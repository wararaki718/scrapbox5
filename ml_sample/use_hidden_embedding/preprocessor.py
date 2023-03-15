from typing import Tuple

import numpy as np
import pandas as pd


class TextPreprocessor:
    def __init__(self):
        pass
    
    def transform(self, df: pd.DataFrame) -> Tuple[pd.Series, np.ndarray]:
        sentences = df.sentence
        y = df.is_counterfactual.values
        return sentences, y
