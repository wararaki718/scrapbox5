from api.schema.request import Item


class Evaluator:
    def __init__(self) -> None:
        pass

    def evaluate(self, item: Item) -> float:
        total = (item.price + len(item.name))
        if total == 0:
            return 0.
        
        return total / 100.0
