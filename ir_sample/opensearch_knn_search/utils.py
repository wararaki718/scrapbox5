from typing import List

from item import Item


def generate_data() -> List[Item]:
    items = [
        {"name": "title1", "vector": [1.5, 5.5, 4.5, 6.4], "price": 10.3},
        {"name": "title2", "vector": [2.5, 3.5, 5.6, 6.7], "price": 5.5},
        {"name": "title3", "vector": [4.5, 5.5, 6.7, 3.7], "price": 4.4},
        {"name": "title4", "vector": [1.5, 5.5, 4.5, 6.4], "price": 8.9},
    ]
    return [Item(**item) for item in items]


def show(hits: List[dict]):
    print("search results:")
    for i, hit in enumerate(hits):
        print(f"result {i}")
        source = hit["_source"]
        print(f"  id={hit['_id']}")
        for key, value in source.items():
            print(f"  {key}={value}")
