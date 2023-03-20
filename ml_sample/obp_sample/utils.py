from typing import Tuple

from obp.dataset import (
    SyntheticBanditDataset,
    logistic_reward_function,
    linear_behavior_policy
)
from obp.types import BanditFeedback


def get_data(n_actions: int, dim_context: int = 3, n_rounds: int = 10000) -> Tuple[BanditFeedback, BanditFeedback, SyntheticBanditDataset]:
    """
    n_actions: k (the number of actions)
    dim_context: dimension of one-hot
    n_rounds: the number of data
    """
    dataset = SyntheticBanditDataset(
        n_actions=n_actions,
        dim_context=dim_context,
        reward_function=logistic_reward_function,
        behavior_policy_function=linear_behavior_policy
    )
    train = dataset.obtain_batch_bandit_feedback(n_rounds=n_rounds)
    valid = dataset.obtain_batch_bandit_feedback(n_rounds=n_rounds)

    return (train, valid, dataset)
