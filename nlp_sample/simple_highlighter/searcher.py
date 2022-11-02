from typing import List

from position import Position
from character import Character


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
        for i in range(len(target_tokens)):
            if target_tokens[i].is_empty() or target_tokens[i] != base_tokens[0]:
                continue
            
            target = ""
            j = 0
            while i+j < len(target_tokens) and len(target) < len(base):
                target += str(target_tokens[i+j])
                j += 1

            #print(f"base={base}, target={target}")
            if target == base:
                position = Position(
                    start = target_tokens[i].base_start,
                    end = target_tokens[i+j-1].base_start + 1 # exclude offset
                )
                #print(target_tokens[i], target_tokens[i].start)
                #print(target_tokens[i+j-1], target_tokens[i+j-1].start)
                positions.append(position)
        return positions
