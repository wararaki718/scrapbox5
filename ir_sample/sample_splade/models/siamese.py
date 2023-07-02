from typing import Dict, Optional

import torch
import torch.nn as nn


def normalize(x: torch.Tensor, eps: float=1e-9) -> torch.Tensor:
    return x / torch.norm(x, dim=-1, keepdim=True)


class SiameseNetwork(nn.Module):
    def __init__(self, query_transformer: nn.Module, document_transformer: nn.Module, match_type: str="dot_product") -> None:
        super().__init__()
        self._query_transformer = query_transformer
        self._document_transformer = document_transformer

        if match_type == "cosine_similarity":
            self._match_function = normalize
        else:
            self._match_function = lambda x: x
        
    def encode(self, tokens: dict, is_q: bool) -> torch.Tensor:
        return self._encode(tokens, is_q)

    def _encode(self, tokens: dict, is_query: bool=False) -> torch.Tensor:
        if is_query:
            return self._query_transformer(**tokens)
        else:
            return self._document_transformer(**tokens)
    
    def train(self, mode: bool=True, is_query: bool=False) -> None:
        if is_query:
            self._query_transformer.train(mode)
        self._document_transformer.train(mode)
    
    def forward(
            self,
            document_words: Optional[dict]=None,
            query_keywords: Optional[dict]=None,
            nb_negatives: Optional[int]=None,
            is_score_batch: bool=False) -> Dict[str, torch.Tensor]:
        out: Dict[str, torch.Tensor] = {}

        if document_words is not None:
            x_document = self.encode(document_words, False)
            x_document = self._match_function(x_document)
            out.update({"d_rep": x_document})
        
        if query_keywords is not None:
            x_query = self.encode(query_keywords, True)
            x_query = self._match_function(x_query)
            out.update({"q_rep": x_query})
        
        if document_words is None or query_keywords is None:
            return out
        
        if nb_negatives is not None:
            x_document = x_document.reshape(x_query.shape[0], nb_negatives, -1)
            x_query = x_query.unsqueeze(1)
            score = torch.sum(x_query * x_document, dim=-1)
        elif is_score_batch:
            score = torch.matmul(x_query, x_document.t())
        else:
            score = torch.sum(x_query, x_document, dim=1, keepdim=True)
        out.update({"score": score})

        return out