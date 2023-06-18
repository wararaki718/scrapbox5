from typing import List

from schema.pair import Pair

MAX_LENGTH = 10

ENG_PREFIXES = (
    "i am ",
    "i m ",
    "he is",
    "he s ",
    "she is",
    "she s ",
    "you are",
    "you re ",
    "we are",
    "we re ",
    "they are",
    "they re "
)


class PairFilter:
    def __init__(self) -> None:
        pass

    def filter(self, pairs: List[Pair]) -> List[Pair]:
        filtered_pairs = []
        for pair in pairs:
            if len(pair.input_.split(" ")) < MAX_LENGTH and len(pair.target.split(" ")) < MAX_LENGTH and pair.target.startswith(ENG_PREFIXES):
                filtered_pairs.append(pair)
        
        return filtered_pairs
