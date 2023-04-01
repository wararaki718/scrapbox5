from typing import List

from .card import GiftCard, GiftCardWithVector


class GiftPostprocessor:
    def __init__(self):
        pass

    def transform(self, cards: List[GiftCard], vectors: List[List[float]]) -> List[GiftCardWithVector]:
        vector_cards = list()
        for card, vector in zip(cards, vectors):
            vector_card = GiftCardWithVector(
                **card.dict(),
                vector=vector
            )
            vector_cards.append(vector_card)

        return vector_cards
