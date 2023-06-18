from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F

from schema.enum import TOKEN
from utils import try_gpu


MAX_LENGTH = 10


class BahdanauAttention(nn.Module):
    def __init__(self, n_hidden: int) -> None:
        super(BahdanauAttention, self).__init__()
        self.Wa = nn.Linear(n_hidden, n_hidden)
        self.Ua = nn.Linear(n_hidden, n_hidden)
        self.Va = nn.Linear(n_hidden, 1)

    def forward(self, query: torch.Tensor, keys: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        scores = self.Va(torch.tanh(self.Wa(query) + self.Ua(keys)))
        scores = scores.squeeze(2).unsqueeze(1)

        weights = F.softmax(scores, dim=-1)
        context = torch.bmm(weights, keys)

        return context, weights


class AttentionDecoder(nn.Module):
    def __init__(self, n_hidden: int, n_output: int, dropout_p: float=0.1) -> None:
        super(AttentionDecoder, self).__init__()
        self.embedding = nn.Embedding(n_output, n_hidden)
        self.attention = BahdanauAttention(n_hidden)
        self.gru = nn.GRU(2 * n_hidden, n_hidden, batch_first=True)
        self.out = nn.Linear(n_hidden, n_output)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self,
                encoder_outputs: torch.Tensor,
                encoder_hidden: torch.Tensor,
                target_tensor: Optional[torch.Tensor]=None
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        batch_size = encoder_outputs.size(0)
        decoder_input = torch.empty(batch_size, 1, dtype=torch.long).fill_(TOKEN.SOS)
        decoder_input = try_gpu(decoder_input)
        decoder_hidden = encoder_hidden
        decoder_outputs = []
        attentions = []

        for i in range(MAX_LENGTH):
            decoder_output, decoder_hidden, attn_weights = self.forward_step(
                decoder_input, decoder_hidden, encoder_outputs
            )
            decoder_outputs.append(decoder_output)
            attentions.append(attn_weights)

            if target_tensor is not None:
                decoder_input = target_tensor[:, i].unsqueeze(1)
            else:
                _, topk = decoder_output.topk(1)
                decoder_input = topk.squeeze(-1).detach()

        decoder_outputs = torch.cat(decoder_outputs, dim=1)
        decoder_outputs = F.log_softmax(decoder_outputs, dim=-1)
        attentions = torch.cat(attentions, dim=1)

        return decoder_outputs, decoder_hidden, attentions


    def forward_step(self,
                     x_input: torch.Tensor,
                     x_hidden: torch.Tensor,
                     encoder_outputs: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        embedded =  self.dropout(self.embedding(x_input))

        query = x_hidden.permute(1, 0, 2)
        context, weights = self.attention(query, encoder_outputs)
        input_gru = torch.cat((embedded, context), dim=2)

        x_output, x_hidden = self.gru(input_gru, x_hidden)
        x_output = self.out(x_output)

        return x_output, x_hidden, weights
