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

        for i in range(len(target_tokens)-len(base_tokens)+1):
            target = "".join(map(str, target_tokens[i:i+len(base_tokens)-1]))
            #print(base, target[:len(base)], target[:len(base)]==base, len(target) - len(base))
            if target[:len(base)] == base:
                offset = len(target) - len(base)
                position = Position(
                    start = target_tokens[i].base_index,
                    end = target_tokens[i+len(base_tokens)-1-offset].base_index
                )
                positions.append(position)

        return positions
