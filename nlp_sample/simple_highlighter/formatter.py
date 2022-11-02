from position import Position


class PositionFormatter:
    def __init__(self):
        pass

    def format(self, position: Position, text: str) -> Position:
        if position.end < len(text) and text[position.end] == "゛":
            position.end += 1
        #print(position, text[position.start:position.end])
        return position
