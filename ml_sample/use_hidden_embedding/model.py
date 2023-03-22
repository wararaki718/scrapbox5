import torch
import torch.nn as nn

from embedding import CustomEmbedding


class NNModel(nn.Module):
    def __init__(self, n_input: int, n_output: int=2, n_hidden: int=10):
        super(NNModel, self).__init__()
        self._embedding = CustomEmbedding(n_input, n_hidden)
        self._linear = nn.Linear(n_hidden, n_output)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self._embedding(x)
        x = torch.sigmoid(x)
        x = self._linear(x)
        return x
