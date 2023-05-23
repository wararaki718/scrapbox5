import json

from qdrant_client.models import VectorParams, Distance, OptimizersConfigDiff

from builder import QueryBuilder
from client import SearchClient
from condition import SearchCondition
from utils import get_data


def main():
    collection_name = "sample"
    dim = 3

    client = SearchClient()
    params = VectorParams(
        size=dim,
        distance=Distance.COSINE
    )
    _ = client.create_index(collection_name, params)
    print(f"index created: {collection_name}")

    points = get_data()
    client.insert(collection_name, points)
    print(f"data inserted: {len(points.ids)}")
    print()

    response = client.get_collection(collection_name)
    print(json.dumps(response.dict(), indent=4))
    print()

    optimizer_config = OptimizersConfigDiff(
        indexing_threshold=10000
    )
    client.update_collection(collection_name=collection_name, optimizer_config=optimizer_config)
    print("update collection config")

    response = client.get_collection(collection_name)
    print(json.dumps(response.dict(), indent=4))
    print()

    print("## search")
    condition = SearchCondition(key="city", value="London")
    query = QueryBuilder.build(condition, vector=[0.3, 0.2, 0.1])
    response = client.search(collection_name, query)
    print(response)

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
