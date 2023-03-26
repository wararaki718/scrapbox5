from typing import Tuple

import torch
import torch.nn as nn


class MLPModel(nn.Module):
    def __init__(self, n_input: int, n_output: int, n_hidden: int = 32) -> None:
        super().__init__()
        self.linear1 = nn.Linear(n_input, n_hidden)
        self.linear2 = nn.Linear(n_hidden, n_hidden)
        self.linear3 = nn.Linear(n_hidden, n_hidden)
        self.linear4 = nn.Linear(n_hidden, n_output)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = nn.functional.elu(self.linear1(x))
        x = nn.functional.elu(self.linear2(x))
        x = nn.functional.elu(self.linear3(x))
        x = self.linear4(x)
        return x.flatten(1)
