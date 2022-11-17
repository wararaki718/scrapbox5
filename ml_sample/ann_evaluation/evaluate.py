import numpy as np


def accuracy_at_k(y_trues: np.ndarray, y_preds: np.ndarray, k: int=10) -> float:
    total = 0
    for y_true, y_pred in zip(y_trues, y_preds):
        total += len(np.intersect1d(y_true[:k], y_pred[:k]))
    
    return total / (y_trues.shape[0]*min(k, y_trues.shape[1]))


def precision_at_k(y_trues: np.ndarray, y_preds: np.ndarray, k: int=10) -> float:
    total = 0.0
    for y_true, y_pred in zip(y_trues, y_preds):
        total += len(np.intersect1d(y_true[:k], y_pred[:k])) / len(y_true[:k])
    return total / len(y_trues)


def recall_at_k(y_trues: np.ndarray, y_preds: np.ndarray, k: int=10) -> float:
    total = 0.0
    for y_true, y_pred in zip(y_trues, y_preds):
        total += len(np.intersect1d(y_true[:k], y_pred[:k])) / len(y_true)
    return total / len(y_trues)


def f_measure_at_k(y_trues: np.ndarray, y_preds: np.ndarray, k: int=10) -> float:
    recall = recall_at_k(y_trues, y_preds, k)
    precision = precision_at_k(y_trues, y_preds, k)
    return (2.0 * recall * precision) / (recall + precision)


def mrr_at_k(y_trues: np.ndarray, y_preds: np.ndarray, k: int=10) -> float:
    total = 0.0
    for y_true, y_pred in zip(y_trues, y_preds):
        for i, y in enumerate(y_pred[:k], start=1):
            if y in y_true:
                total += (1.0 / i)
                break
    return total / len(y_trues)


def map_at_k(y_trues: np.ndarray, y_preds: np.ndarray, k: int=10) -> float:
    total = 0.0
    for i in range(1, k+1):
        total += precision_at_k(y_trues, y_preds, i)
    return total / len(y_trues)
