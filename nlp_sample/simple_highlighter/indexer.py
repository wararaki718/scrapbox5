from typing import List

from character import Character


class CharacterIndexer:
    def index(self, text: str) -> List[Character]:
        return [
            Character(
                base_start=i,
                fixed_start=i,
                base_char=c,
                fixed_char=c
            )
            for i, c in enumerate(list(text))
        ]
