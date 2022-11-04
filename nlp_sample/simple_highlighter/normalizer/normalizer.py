import copy
from typing import List

from .eliminater import EmptyCharacterEliminator
from .encoder import DakutenEncoder
from schema import Character


class CharacterNormalizer:
    def __init__(self):
        self._encoder = DakutenEncoder()
        self._eliminator = EmptyCharacterEliminator()

    def normalize(self, tokens: List[Character]) -> List[Character]:
        tokens = copy.deepcopy(tokens) # memory cost
        tokens = self._encoder.encode(tokens)
        tokens = self._eliminator.eliminate(tokens)
        return tokens
