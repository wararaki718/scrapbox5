from typing import List

from schema import Character


class EmptyCharacterEliminator:
    def eliminate(self, tokens: List[Character]) -> List[Character]:
        return list(filter(lambda token: not token.is_empty(), tokens))
