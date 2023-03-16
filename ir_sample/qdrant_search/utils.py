from qdrant_client.http.models import Batch


def get_data() -> Batch:
    points = Batch(
        ids=[1, 2, 3, 4, 5, 6],
        payloads=[
            {"color": "green", "city": "London"},
            {"color": "red", "city": "London"},
            {"color": "blue", "city": "London"},
            {"color": "red", "city": "Berlin"},
            {"color": "green", "city": "Moscow"},
            {"color": "blue", "city": "Moscow"}
        ],
        vectors=[
            [0.1, 0.9, 0.1],
            [0.9, 0.1, 0.1],
            [0.1, 0.1, 0.9],
            [0.9, 0.1, 0.1],
            [0.1, 0.9, 0.1],
            [0.1, 0.1, 0.9]
        ]
    )
    return points
