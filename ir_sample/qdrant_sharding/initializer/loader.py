import json
from pathlib import Path
from typing import List

from .card import GiftCard


class GiftCardLoader:
    def __init__(self):
        pass

    def load(self, filepath: Path) -> List[GiftCard]:
        cards = list()
        with open(filepath) as f:
            for line in f:
                card = json.loads(line)
                cards.append(GiftCard(**card))
        return cards[:256]
