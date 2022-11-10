from typing import List

from schema import Character


class CharacterIndexer:
    def index(self, text: str) -> List[Character]:
        return [
            Character(
                index=i,
                value=c
            )
            for i, c in enumerate(list(text) + ["EOF"])
        ]
