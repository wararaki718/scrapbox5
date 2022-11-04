from typing import List

from schema import Character, Position


class PositionSearcher:
    def search(self, base_tokens: List[Character], target_tokens: List[Character]) -> List[Position]:
        """
        base_tokens: keyword
        target_tokens: text
        """
        positions = []
        base = "".join(map(str, base_tokens))
        target = "".join(map(str, target_tokens))

        for i in range(len(target)-len(base)+1):
            if target[i:i+len(base)] == base:
                position = Position(
                    start = target_tokens[i].base_index,
                    end = target_tokens[i+len(base)].base_index
                )
                positions.append(position)

        return positions
