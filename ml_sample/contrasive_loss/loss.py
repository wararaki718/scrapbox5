import torch
import torch.nn as nn

from distance import euclidean_distance, l1_distance


class ContrasiveLoss(nn.Module):
    def __init__(self, margin: float=1.0, distance: str="euclidean") -> None:
        super(ContrasiveLoss, self).__init__()

        if distance == "euclidean":
            self._distance = euclidean_distance
        elif distance == "l1":
            self._distance = l1_distance
        else:
            raise RuntimeError
        
        self._margin = margin
    
    def __call__(self, y_true: torch.Tensor, y_pred: torch.Tensor) -> torch.Tensor:
        # y_true=0 is same class
        # y_true=1 is different class.
        D = self._distance(y_true, y_pred)
        L = (1. - y_true.flatten()) * 0.5 * D**2 + y_true.flatten() * 0.5 * torch.relu(self._margin - D) ** 2
        return L
