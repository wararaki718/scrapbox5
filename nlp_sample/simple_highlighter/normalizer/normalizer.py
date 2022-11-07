import copy
from typing import List

from .eliminater import EmptyCharacterEliminator
from .encoders import DakutenEncoder, SuujiEncoder
from schema import Character


class CharacterNormalizer:
    def __init__(self):
        self._dakuten_encoder = DakutenEncoder()
        self._suuji_encoder = SuujiEncoder()
        self._eliminator = EmptyCharacterEliminator()

    def normalize(self, tokens: List[Character]) -> List[Character]:
        tokens = copy.deepcopy(tokens) # memory cost
        tokens = self._dakuten_encoder.encode(tokens)
        tokens = self._suuji_encoder.encode(tokens)
        tokens = self._eliminator.eliminate(tokens)
        return tokens
