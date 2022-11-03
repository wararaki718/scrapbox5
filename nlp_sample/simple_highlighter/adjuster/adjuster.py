from typing import List

from model import Position


class PositionAdjuster:
    def __init__(self):
        pass

    def _adjust(self, position: Position, text: str) -> Position:
        # dakuten
        if position.end < len(text) and text[position.end] == "゛":
            position.end += 1
        return position

    def adjust(self, positions: List[Position], text: str) -> List[Position]:
        return [self._adjust(position, text) for position in positions]
