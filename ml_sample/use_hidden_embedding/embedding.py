import torch
import torch.nn as nn


class CustomEmbedding(nn.Module):
    def __init__(self, n_input: int, n_output: int, n_hidden: int = 10):
        super(CustomEmbedding, self).__init__()
        self._linear1 = nn.Linear(n_input, n_hidden)
        self._linear2 = nn.Linear(n_hidden, n_output)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self._linear1(x)
        x = self._linear2(x)
        return x
