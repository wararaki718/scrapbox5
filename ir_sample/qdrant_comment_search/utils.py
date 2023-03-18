from typing import List, Union

import torch
from transformers import AutoModel
from qdrant_client.models import ScoredPoint


def try_gpu(x: Union[torch.Tensor, AutoModel]) -> Union[torch.Tensor, AutoModel]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x


def show(results: List[ScoredPoint]):
    for result in results:
        print("----")
        print(result.id)
        print(result.payload["sentence_id"])
        print(result.payload["sentence"])
        print(result.score)
    print()
