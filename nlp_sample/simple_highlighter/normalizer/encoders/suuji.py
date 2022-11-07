from typing import List

from schema import Character


class SuujiEncoder:
    def encode(self, tokens: List[Character]) -> List[Character]:
        n = len(tokens)
        for i in range(n-1, -1, -1):
            if str(tokens[i]) == "X":
                tokens[i].fixed_char = "1"
                tokens.insert(i+1, Character(base_index=tokens[i].base_index, fixed_char="0"))
        return tokens
