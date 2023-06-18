from typing import List


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

    def filter(self, pairs: List[List[str]]) -> List[List[str]]:
        filtered_pairs = []
        for pair in pairs:
            if len(pair[0].split(" ")) < MAX_LENGTH and len(pair[1].split(" ")) < MAX_LENGTH and pair[0].startswith(ENG_PREFIXES):
                filtered_pairs.append(pair)
        
        return filtered_pairs
