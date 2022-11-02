from typing import List

from character import Character


class DakutenNormalizer:
    def __init__(self):
        self._dakuten_maps = {
            key: value
            for key, value in zip(list("カキクケコ"), list("ガギグゲゴ"))
        }

    def normalize(self, tokens: List[Character]) -> List[Character]:
        index = 1
        for i in range(1, len(tokens)):
            c = self._dakuten_maps.get(str(tokens[i - 1]))
            if "゛" != str(tokens[i]) and c is None:
                continue
            tokens[i].fixed_char = ""
            tokens[i-1].fixed_char = c
            tokens[i-1].fixed_index -= index
            index += 1
            
        return tokens


class CharacterNormalizer:
    def __init__(self):
        self._dakuten = DakutenNormalizer()

    def normalize(self, tokens: List[Character]) -> List[Character]:
        return self._dakuten.normalize(tokens)
