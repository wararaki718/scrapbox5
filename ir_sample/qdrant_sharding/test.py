from typing import List

from qdrant_client.models import ScoredPoint

from search import QdrantSearch


def show(response: List[ScoredPoint]):
    for i, point in enumerate(response, start=1):
        print(f"#{i}: id={point.id}, score={point.score}")


def main():
    #collection_name = "reviews"
    collection_name = "reviews_shard"
    search_client = QdrantSearch()

    response = search_client.search(collection_name)
    show(response)
    print("DONE")


if __name__ == "__main__":
    main()
