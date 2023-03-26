from time import sleep

from qdrant_client.models import VectorParams

from builder import QueryBuilder
from client import SearchClient
from utils import get_data, show


def main():
    collection_name = "sample"
    dim = 3

    client = SearchClient()
    params = VectorParams(
        size=dim,
        distance="Cosine"
    )
    _ = client.create_index(collection_name, params)
    print(f"index created: {collection_name}")
    sleep(1)

    points = get_data()
    client.insert(collection_name, points)
    print(f"data inserted: {len(points.ids)}")
    sleep(1)

    # prefilter
    query = QueryBuilder.build(key="city", value="London", vector=[0.9, 0.1, 0.1])
    response = client.search(collection_name, query)
    show(response)
    sleep(1)

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
