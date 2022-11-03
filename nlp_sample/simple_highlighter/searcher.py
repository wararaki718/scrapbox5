from typing import List

from model import Character, Position


class PositionSearcher:
    def __init__(self):
        pass

    def search(self, base_tokens: List[Character], target_tokens: List[Character]) -> List[Position]:
        """
        base_tokens: keyword
        target_tokens: text
        """
        positions = []
        base = "".join(map(str, base_tokens))
        target = "".join(map(str, target_tokens[:len(base)-1]))

        for i, token in enumerate(target_tokens[len(target):]):
            target += str(token)
            if target == base:
                position = Position(
                    start = target_tokens[i].base_index,
                    end = target_tokens[i+len(target)-1].base_index + 1 # add exclude offset
                )
                positions.append(position)
            target = target[1:]

        return positions
