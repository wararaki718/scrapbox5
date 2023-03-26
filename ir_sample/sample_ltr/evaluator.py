import torch
from sklearn.metrics import ndcg_score

from model import MLPModel
from utils import try_gpu, convert_gamma_to_implicit


class LTREvaluator:
    def __init__(self):
        pass

    def evaluate(self, model: MLPModel, X_test: torch.Tensor, y_true: torch.Tensor) -> float:
        model.eval()
        with torch.no_grad():
            y_preds = model(try_gpu(X_test))
        
        y_true, _ = convert_gamma_to_implicit(y_true.reshape(-1, 1), pow_true=0.0)
        print(y_true.cpu().detach().numpy().shape)
        print(y_preds.cpu().detach().numpy().shape)
        return ndcg_score(
            y_true.cpu().detach().numpy().reshape(1, -1),
            y_preds.cpu().detach().numpy().reshape(1, -1),
            k=10
        )
