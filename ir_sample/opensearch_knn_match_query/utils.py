from typing import List, Union

import torch
from transformers import AutoModel


def try_gpu(x: Union[torch.Tensor, AutoModel]) -> Union[torch.Tensor, AutoModel]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x


def show(keyword: str, hits: List[dict]):
    print(f"search results [keyword={keyword}]:")
    for i, hit in enumerate(hits):
        print(f"result {i}")
        source = hit["_source"]
        print(f"  id={hit['_id']}")
        print(f"  newsid={source['newsid']}")
        print(f"  context={source['context'][:30]}...")
        print()
    print()
