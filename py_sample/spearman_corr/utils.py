import random
from typing import List, Tuple


def get_two_ranks(n: int=10) -> Tuple[List[int], List[int]]:
    ranks = [i for i in range(1, n+1)]
    predicts = [i for i in range(1, n+1)]
    random.shuffle(predicts)

    return ranks, predicts
