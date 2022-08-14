from typing import List, Union

import torch
from transformers import AutoModel


def try_gpu(x: Union[torch.Tensor, AutoModel]) -> Union[torch.Tensor, AutoModel]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x


def show(hits: List[dict]):
    for hit in hits:
        source = hit["_source"]
        print(source["version_id"])
        print(source["wikidata_id"])
        print(source["text"])
        print()
