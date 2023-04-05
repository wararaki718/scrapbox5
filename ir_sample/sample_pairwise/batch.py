from typing import Generator, List, Tuple

import pandas as pd
import torch


class BatchIterator:
    def __init__(self, X: List[torch.Tensor], y: List[torch.Tensor], df: List[pd.DataFrame]):
        self._X = X
        self._y = y
        self._df = df

    def __iter__(self) -> Generator[Tuple[torch.Tensor, torch.Tensor, pd.DataFrame], None, None]:
        for X, y, df in zip(self._X, self._y, self._df):
            yield (X, y, df)
    
    def __len__(self) -> int:
        return len(self._X)

    def shape(self):
        print((len(self._X), self._X[0].shape[1]))
        print((len(self._y),))
        print((len(self._df), self._df[0].shape[1]))

    def get_n_features(self) -> int:
        return self._X[0].shape[1]
