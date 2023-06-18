from typing import Union

import torch


def try_gpu(x: Union[torch.Tensor, torch.Module]) -> Union[torch.Tensor, torch.Module]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x
