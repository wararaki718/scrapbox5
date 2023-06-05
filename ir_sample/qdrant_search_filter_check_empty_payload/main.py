from qdrant_client.models import VectorParams

from builder import QueryBuilder
from client import SearchClient
from condition import SearchCondition
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

    points = get_data()
    client.insert(collection_name, points)
    print(f"data inserted: {len(points.ids)}")

    # prefilter
    condition = SearchCondition(
        city="London"
    )
    query = QueryBuilder.build(condition=condition, vector=[0.9, 0.1, 0.1])
    response = client.search(collection_name, query)
    show(response)

    condition = SearchCondition(
        color="blue"
    )
    query = QueryBuilder.build(condition=condition, vector=[0.9, 0.1, 0.1])
    response = client.search(collection_name, query)
    show(response)

    condition = SearchCondition()
    query = QueryBuilder.build(condition=condition, vector=[0.9, 0.1, 0.1])
    response = client.search(collection_name, query)
    show(response)

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
