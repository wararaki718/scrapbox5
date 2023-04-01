from typing import List

from .card import GiftCard


class TextPreprocessor:
    def __init__(self):
        pass

    def transform(self, cards: List[GiftCard]) -> List[str]:
        texts = list()

        for card in cards:
            text = " ".join(filter(lambda x: x is not None, [card.summary, card.reviewText]))
            texts.append(text)
        
        return texts
