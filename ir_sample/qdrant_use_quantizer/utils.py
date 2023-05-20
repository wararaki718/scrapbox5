from typing import List

from qdrant_client.models import ScoredPoint


def show(results: List[ScoredPoint]):
    for result in results:
        print("----")
        print(result.id)
        print(result.payload["sentence_id"])
        print(result.payload["sentence"])
        print(result.score)
    print()
