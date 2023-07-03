from typing import Optional

import torch
import torch.nn as nn

from .siamese import SiameseNetwork


class SpladeModel(nn.Module):
    def __init__(
            self,
            query_transformer: nn.Module,
            document_transformer: nn.Module,
            match_type: str="dot_product",
            agg_type: str="max") -> None:
        super(SpladeModel).__init__()
        self._query_model = SiameseNetwork(query_transformer, match_type, agg_type)
        self._document_model = SiameseNetwork(document_transformer, match_type, agg_type)

    def forward(
            self,
            query_tokens: dict,
            document_tokens: dict,
            nb_negatives: Optional[int]=None,
            is_score_batch: bool=False) -> torch.Tensor:
        x_query: torch.Tensor = self._query_model(query_tokens)
        x_document: torch.Tensor = self._document_model(document_tokens)

        if nb_negatives is not None:
            x_document = x_document.reshape(x_query.shape[0], nb_negatives, -1)
            x_query = x_query.unsqueeze(1)
            score = torch.sum(x_query * x_document, dim=-1)
        elif is_score_batch:
            score = torch.matmul(x_query, x_document.t())
        else:
            score = torch.sum(x_query, x_document, dim=1, keepdim=True)
        
        return score
