from typing import List

from qdrant_client.http.models import Batch, ScoredPoint


def get_data1() -> Batch:
    points = Batch(
        ids=[1, 2, 3],
        payloads=[
            {"color": "green", "city": "London"},
            {"color": "red", "city": "London"},
            {"color": "blue", "city": "London"}
        ],
        vectors=[
            [0.1, 0.9, 0.1],
            [0.9, 0.1, 0.1],
            [0.1, 0.1, 0.9]
        ]
    )
    return points


def get_data2() -> Batch:
    points = Batch(
        ids=[4, 5, 6],
        payloads=[
            {"color": "red", "city": "Berlin"},
            {"color": "green", "city": "Moscow"},
            {"color": "blue", "city": "Moscow"}
        ],
        vectors=[
            [0.9, 0.1, 0.1],
            [0.1, 0.9, 0.1],
            [0.1, 0.1, 0.9]
        ]
    )
    return points


def show(points: List[ScoredPoint]):
    print("###")
    for point in points:
        print(point)
    print("###")
    print()

