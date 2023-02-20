from typing import Union

import torch
from transformers import AutoModel


def try_gpu(x: Union[torch.Tensor, AutoModel]) -> Union[torch.Tensor, AutoModel]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x
