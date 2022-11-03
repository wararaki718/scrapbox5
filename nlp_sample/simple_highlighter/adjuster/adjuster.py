from model import Position


class PositionAdjuster:
    def __init__(self):
        pass

    def adjust(self, position: Position, text: str) -> Position:
        # dakuten
        if position.end < len(text) and text[position.end] == "゛":
            position.end += 1
        return position
