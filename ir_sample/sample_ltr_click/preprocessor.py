import pandas as pd
import torch

from batch import BatchIterator


class LTRPreprocessor:
    def transform(self, df: pd.DataFrame) -> BatchIterator:
        columns = ["qid", "label", "label_norm", "docid", "inc", "prob"]
        feature_columns = list(set(df.columns) - set(columns))

        X = []
        y = []
        dfs = []
        for qid in df.qid:
            tmp = df[df.qid == qid]
            X.append(torch.Tensor(tmp[feature_columns].values))
            y.append(torch.Tensor(tmp[["label_norm"]].values))
            dfs.append(tmp[columns].copy())

        return BatchIterator(X, y, dfs)
