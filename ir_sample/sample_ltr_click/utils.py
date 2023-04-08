from typing import Tuple, Union

import torch


def try_gpu(x: Union[torch.Tensor, torch.nn.Module]) -> Union[torch.Tensor, torch.nn.Module]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x


# 0-5 scores -> 0-1 clicks convert
def convert_gamma_to_implicit(relevances: torch.Tensor, eps: float=0.1, max_rel: int=4, pow_true: float=1.0, pow_used: float=1.0) -> Tuple[torch.Tensor, torch.Tensor]:
    gamma = 1.0 - eps
    gamma *= (2 ** relevances.float()) - 1
    gamma /= (2 ** max_rel) - 1
    gamma += eps

    theta_true = (0.9 / torch.arange(1, gamma.shape[1] + 1)) ** pow_true
    theta_used = (0.9 / torch.arange(1, gamma.shape[1] + 1)) ** pow_used
    clicks = torch.bernoulli(gamma * theta_true)
    return clicks, theta_used
