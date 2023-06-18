from typing import Tuple

import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, n_input: int, n_hidden: int, dropout: float=0.1) -> None:
        super(Encoder, self).__init__()
        self.embedding = nn.Embedding(n_input, n_hidden)
        self.gru = nn.GRU(n_hidden, n_hidden, batch_first=True)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        x = self.embedding(x)
        x = self.dropout(x)
        output, hidden = self.gru(x)
        return output, hidden
