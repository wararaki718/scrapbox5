import numpy as np
import pandas as pd
from sklearn.metrics import ndcg_score


def ndcg(y_true: np.ndarray, y_pred: np.ndarray, queries: np.ndarray, k: int=10) -> float:
    df = pd.DataFrame({
        "qid": np.repeat(np.arange(queries.shape[0]), queries.astype(np.int16)),
        "pred": y_pred,
        "true": y_true
    })

    return df.groupby("qid").apply(lambda rank: ndcg_score([rank.true], [rank.pred], k=k)).mean()
