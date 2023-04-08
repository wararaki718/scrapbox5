from typing import Optional

import torch


def listwise_loss(scores: torch.Tensor, clicks: torch.Tensor, theta: Optional[torch.Tensor]=None) -> float:
    if theta is None:
        theta = torch.ones_like(clicks)
    
    loss = - (clicks/theta) * torch.nn.functional.log_softmax(scores, dim=0)
    return loss.sum(1).mean()
