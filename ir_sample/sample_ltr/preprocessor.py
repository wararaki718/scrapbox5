from typing import Tuple

import pandas as pd
import torch

from utils import try_gpu


class LTRPreprocessor:
    def transform(self, df: pd.DataFrame) -> Tuple[torch.Tensor, torch.Tensor, pd.DataFrame]:
        columns = ["qid", "label", "label_norm", "docid", "inc", "prob"]
        feature_columns = set(df.columns) - set(columns)

        X = torch.Tensor(df[feature_columns].values)
        y = torch.Tensor(df["label_norm"].values)

        return try_gpu(X), try_gpu(y), df[columns]
