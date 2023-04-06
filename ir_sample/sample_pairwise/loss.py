from typing import Optional

import torch


def listwise_loss(scores: torch.Tensor, clicks: torch.Tensor, theta: Optional[torch.Tensor]=None) -> float:
    if theta is None:
        theta = torch.ones_like(clicks)
    
    loss = - (clicks/theta) * torch.nn.functional.log_softmax(scores, dim=0)
    return loss.sum(1).mean()



def ranknet_loss(y1: torch.Tensor, y2: torch.Tensor, y1_preds: torch.Tensor, y2_preds: torch.Tensor) -> torch.Tensor:
    y_preds_diff = (y1_preds - y2_preds)
    y_diff = (y1 - y2).sign()
    loss = (1. - y_diff) * y_preds_diff / 2. + torch.log(1. + torch.exp(-y_preds_diff))
    return loss.sum()
