from typing import List

from schema import Character


class DakutenEncoder:
    def __init__(self):
        self._dakuten_maps = {
            key: value
            for key, value in zip(list("カキクケコはひふへほ"), list("ガギグゲゴばびぶべぼ"))
        }

    def encode(self, tokens: List[Character]) -> List[Character]:
        for i in range(1, len(tokens)):
            c = self._dakuten_maps.get(str(tokens[i - 1]))
            if "゛" != str(tokens[i]) or c is None:
                continue
            tokens[i].fixed_char = ""
            tokens[i-1].fixed_char = c
        return tokens
