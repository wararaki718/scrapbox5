import torch
import torch.nn as nn


def normalize(x: torch.Tensor, eps: float=1e-9) -> torch.Tensor:
    return x / (torch.norm(x, dim=-1, keepdim=True) + eps)


def agg_max(x: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
    values, _ = torch.max(
        torch.log(1 + torch.relu(x)) * attention_mask.unsqueeze(-1),
        dim=1
    )
    return values


def agg_sum(x: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
    return torch.sum(
        torch.log(1 + torch.relu(x)) * attention_mask.unsqueeze(-1),
        dim=1
    )


class SiameseNetwork(nn.Module):
    def __init__(self, transformer: nn.Module, match_type: str="dot_product", agg_type: str="max") -> None:
        super(SiameseNetwork).__init__()
        self._transformer = transformer

        if match_type == "cosine_similarity":
            self._match_function = normalize
        else:
            self._match_function = lambda x: x
        
        if agg_max == "max":
            self._agg_function = agg_max
        else:
            self._agg_function = agg_sum

    def train(self, mode: bool=True) -> None:
        self._transformer.train(mode)

    def forward(self, tokens: dict) -> torch.Tensor:
        x = self._transformer(tokens)
        x = self._agg_function(x["logits"], tokens["attention_mask"])
        x = self._match_function(x)
        return x
