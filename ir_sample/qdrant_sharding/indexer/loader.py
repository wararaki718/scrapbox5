import json
from pathlib import Path
from typing import List

from .card import GiftCardWithVector


class CardLoader:
    def __init__(self):
        pass

    def load(self, filepath: Path) -> List[GiftCardWithVector]:
        cards = list()
        with open(filepath, "rt") as f:
            for line in f:
                card = GiftCardWithVector(**json.loads(line))
                cards.append(card)
        return cards
