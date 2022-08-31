import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
    
    def push(self, item: int):
        heapq.heappush(self._queue, item)
    
    def pop(self) -> int:
        return heapq.heappop(self._queue)
    
    def __str__(self) -> str:
        return str(self._queue)


def main():
    items = [5, 2, 1, 6, 4, 3]
    print(f"items : {str(items)}")

    pqueue = PriorityQueue()
    for item in items:
        pqueue.push(item)
    
    print(f"pqueue: [{pqueue}]")

    _ = pqueue.pop()
    _ = pqueue.pop()

    print(f"popped pqueue: [{pqueue}]")

    print("DONE")


if __name__ == "__main__":
    main()
