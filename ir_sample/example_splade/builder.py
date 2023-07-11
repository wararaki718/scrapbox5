from typing import Dict

import torch


class SearchIndexBuilder:
    @classmethod
    def build(cls, vectors: torch.Tensor, vocabs: Dict[str, int]) -> Dict[str, float]:
        columns = vectors.nonzero().squeeze().cpu().tolist()
        weights = vectors[columns].cpu().tolist()
        features: Dict[str, float] = dict(zip(columns, weights))

        index2token = {
            index: token for token, index in vocabs
        }

        search_index = {
            index2token[index]: weight for index, weight in zip(columns, weights)
        }

        return search_index
