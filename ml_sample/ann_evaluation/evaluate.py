import numpy as np


def accuracy_at_n(y_trues: np.ndarray, y_preds: np.ndarray, at_n: int=10) -> float:
    if y_trues.shape != y_preds.shape:
        raise TypeError("shape error")
    
    total = 0
    for y_true, y_pred in zip(y_trues, y_preds):
        total += len(set(y_true[:at_n])&set(y_pred[:at_n]))
    
    return total / (y_trues.shape[0]*min(at_n, y_trues.shape[1]))
