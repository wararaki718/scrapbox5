from typing import List

import numpy as np


def get_vector(n: int, d: int) -> np.ndarray:
    x = np.random.random((n, d)).astype(np.float32)
    return x


def get_data(n: int) -> List[dict]:
    data = []
    for i in range(1, n+1):
        item = {
            "title": f"title_{i}",
            "content": f"content_{i}"
        }
        data.append(item)
    
    return data


def show(results: list):
    for result in results:
        print(f"id     : {result.id}")
        print(f"score  : {result.score}")
        print(f"payload: {result.payload}")
    print()
