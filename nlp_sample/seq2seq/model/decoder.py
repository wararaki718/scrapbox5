from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F

from schema.enum import TOKEN
from utils import try_gpu


MAX_LENGTH = 10


class Decoder(nn.Module):
    def __init__(self, n_hidden: int, n_output: int) -> None:
        super(Decoder, self).__init__()
        self.embedding = nn.Embedding(n_output, n_hidden)
        self.gru = nn.GRU(n_hidden, n_hidden, batch_first=True)
        self.linear = nn.Linear(n_hidden, n_output)
    
    def forward(self,
                encoder_outputs: torch.Tensor,
                encoder_hidden: torch.Tensor,
                target_tensor: Optional[torch.Tensor]=None
    ) -> Tuple[torch.Tensor, torch.Tensor, None]:
        batch_size = encoder_outputs.size(0)
        decoder_input = torch.empty(batch_size, 1, dtype=torch.long).fill_(TOKEN.SOS)
        decoder_input = try_gpu(decoder_input)
        decoder_hidden = encoder_hidden
        decoder_outputs = []

        for i in range(MAX_LENGTH):
            decoder_output, decoder_hidden = self.forward_step(decoder_input, decoder_hidden)
            decoder_outputs.append(decoder_output)

            if target_tensor is not None:
                decoder_input = target_tensor[:, i].unsqueeze(1)
            else:
                _, topk = decoder_output.topk(1)
                decoder_input = topk.squeeze(-1).detach()

        decoder_outputs = torch.cat(decoder_outputs, dim=1)
        decoder_outputs = F.log_softmax(decoder_outputs, dim=-1)
        return decoder_outputs, decoder_hidden, None

    def forward_step(self, x_input: torch.Tensor, x_hidden: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        x_output = self.embedding(x_input)
        x_output = F.relu(x_output)
        x_output, x_hidden = self.gru(x_output, x_hidden)
        x_output = self.linear(x_output)
        return x_output, x_hidden
