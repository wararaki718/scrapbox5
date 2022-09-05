import random
from queue import PriorityQueue

class Sample:
    def __init__(self, _id: int, weight: float):
        self._id = _id
        self._weight = weight
    
    def __str__(self) -> str:
        return f"id={self._id}, weight={self._weight}"
    
    def __lt__(self, sample: "Sample") -> bool:
        return self._weight < sample._weight


def solve(items: list) -> list:
    pque = PriorityQueue()
    for item in items:
        pque.put(item)
    
    results = []
    while not pque.empty():
        result = pque.get()
        results.append(result)

    return results


def main():
    print("primitive type")
    a = [1, 5, 2, 6, 3, 4]
    b = solve(a)
    
    print(f"before: {a}")
    print(f"after : {b}")
    print()

    print("class object")
    c = []
    for i in range(6):
        item = Sample(_id=i, weight=random.random())
        c.append(item)
    d = solve(c)

    c_ids = [item._id for item in c]
    c_weights = [item._weight for item in c]
    d_ids = [item._id for item in d]
    d_weights = [item._weight for item in d]
    
    print(f"before:")
    print(f"ids={c_ids}")
    print(f"weights={c_weights}")
    print(f"ids={d_ids}")
    print(f"weights={d_weights}")
    print()

    print("DONE")


if __name__ == "__main__":
    main()
