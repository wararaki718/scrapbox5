from typing import List

from qdrant_client.models import ScoredPoint


def show(results: List[ScoredPoint]) -> None:
    for result in results:
        if result.payload is None:
            continue

        print("----")
        print(result.id)
        print(result.payload["sentence_id"])
        print(result.payload["sentence"])
        print(result.score)
    print()
