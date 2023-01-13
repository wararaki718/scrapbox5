from typing import List

from schema import Character, LinkType


class SuujiEncoder:
    def encode(self, tokens: List[Character]) -> List[Character]:
        n = len(tokens)
        for i in range(n-1, -1, -1):
            if str(tokens[i]) == "X":
                tokens[i].value = "1"
                tokens[i].link = LinkType.HEAD
                tokens.insert(i+1, Character(index=tokens[i].index, value="0", link=LinkType.TAIL))
        return tokens
