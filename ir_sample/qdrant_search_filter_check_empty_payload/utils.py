from typing import List

from qdrant_client.http.models import Batch, ScoredPoint


def show(results: List[ScoredPoint]):
    for result in results:
        print(result)
    print()


def get_data() -> Batch:
    points = Batch(
        ids=[1, 2, 3, 4, 5, 6, 7],
        payloads=[
            {"color": "green", "city": "London"},
            {"color": "red", "city": "London"},
            {"color": "red", "city": "Moscow"},
            {"color": "blue"},
            {"color": None, "city": "Tokyo"},
            {"color": "yellow", "city": None},
            {"city": "Osaka"},
        ],
        vectors=[
            [0.1, 0.9, 0.1],
            [0.9, 0.1, 0.1],
            [0.9, 0.1, 0.1],
            [0.1, 0.9, 0.1],
            [0.9, 0.1, 0.1],
            [0.9, 0.1, 0.1],
            [0.5, 0.1, 0.1]
        ]
    )
    return points
