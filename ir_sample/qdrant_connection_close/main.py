from qdrant_client.models import VectorParams

from client import SearchClient
from builder import QueryBuilder
from utils import get_data, show


def main():
    collection_name = "sample"
    client = SearchClient(host="localhost", grpc_port=6334)

    params = VectorParams(
        size=3,
        distance="Cosine"
    )
    _ = client.create_index(collection_name, params)
    print(f"'{collection_name}' is created!")

    points = get_data()
    client.insert(collection_name, points)
    print(f"data inserted: {len(points.ids)}")

    query = QueryBuilder.build(key="city", value="London", vector=[0.3, 0.2, 0.1])
    response = client.search(collection_name, query)
    show(response)

    _ = client.delete_index(collection_name)
    print(f"'{collection_name}' is deleted.")

    print("DONE")


if __name__ == "__main__":
    main()
