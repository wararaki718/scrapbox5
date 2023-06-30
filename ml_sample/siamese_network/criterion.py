import torch
import torch.nn as nn
import torch.nn.functional as F


class ContrasiveLoss(nn.Module):
    def __init__(self, margin: float=2.0) -> None:
        super(ContrasiveLoss, self).__init__()
        self._margin = margin
    
    def forward(self, output1: torch.Tensor, output2: torch.Tensor, label: torch.Tensor) -> torch.Tensor:
        distance = F.pairwise_distance(output1, output2, keepdim=True)
        loss = torch.mean(
            (1 - label) * torch.pow(distance, 2) + label * torch.pow(torch.clamp(self._margin - distance, min=0.0), 2)
        )
        return loss
