import torch
from sklearn.metrics import ndcg_score

from batch import BatchIterator
from model import MLPModel
from utils import try_gpu, convert_gamma_to_implicit


class LTREvaluator:
    def __init__(self):
        pass

    def evaluate(self, model: MLPModel, batch_iter: BatchIterator) -> float:
        scores = 0.0
        model.eval()
        for X, y, _ in batch_iter:
            X_test = try_gpu(X)
            with torch.no_grad():
                y_preds = model(try_gpu(X_test))
            
            y_true, _ = convert_gamma_to_implicit(y.reshape(-1, 1), pow_true=0.0)
            scores += ndcg_score(
                y_true.cpu().detach().numpy().reshape(1, -1),
                y_preds.cpu().detach().numpy().reshape(1, -1),
                k=10
            )
        return scores / len(batch_iter)
