from typing import List

from model import Character


class CharacterIndexer:
    def index(self, text: str) -> List[Character]:
        return [
            Character(
                base_index=i,
                fixed_char=c
            )
            for i, c in enumerate(list(text))
        ]
