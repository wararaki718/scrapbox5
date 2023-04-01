import json
from pathlib import Path
from typing import List

from card import GiftCardWithVector


class GiftCardDumper:
    def __init__(self):
        pass

    def dump(self, cards: List[GiftCardWithVector], filepath: Path):
        with open(filepath, "wt") as f:
            f.writelines(map(lambda data: f"{json.dumps(data)}\n", map(lambda card: card.dict(), cards)))
