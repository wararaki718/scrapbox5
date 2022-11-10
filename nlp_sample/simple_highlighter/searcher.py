from typing import List

from schema import Character, LinkType, Position


class PositionSearcher:
    def search(self, base_tokens: List[Character], target_tokens: List[Character]) -> List[Position]:
        """
        base_tokens: keyword
        target_tokens: text
        """
        positions = []
        base = "".join(map(str, base_tokens))
        target = "".join(map(str, target_tokens))

        #print(base)
        #print(target)
        for i in range(len(target)-len(base)+1):
            if (target_tokens[i].link == LinkType.NODE
                or target_tokens[i].link == LinkType.TAIL
                or target_tokens[i+len(base)-1].link == LinkType.HEAD
                or target_tokens[i+len(base)-1].link == LinkType.NODE):
                continue

            #print(base, target[i:i+len(base)], target[i:i+len(base)]==base)
            #print(target_tokens[i].link, target_tokens[i+len(base)-1].link)

            if target[i:i+len(base)] == base:
                position = Position(
                    start = target_tokens[i].index,
                    end = target_tokens[i+len(base)].index
                )
                positions.append(position)

        return positions
