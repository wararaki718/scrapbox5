from qdrant_client.models import VectorParams

from client import SearchClient
from builder import QueryBuilder
from utils import get_data1, get_data2, show


def main():
    alias_name = "target"
    collection_name1 = "sample"
    collection_name2 = "test"
    client = SearchClient(host="localhost", grpc_port=6334)

    params = VectorParams(
        size=3,
        distance="Cosine"
    )
    _ = client.create_index(collection_name1, params)
    print(f"'{collection_name1}' is created!")

    _ = client.create_index(collection_name2, params)
    print(f"'{collection_name2}' is created!")

    points = get_data1()
    client.insert(collection_name1, points)
    print(f"data inserted: {len(points.ids)}")
    
    points = get_data2()
    client.insert(collection_name2, points)
    print(f"data inserted: {len(points.ids)}")

    query = QueryBuilder.build(key="color", value="red", vector=[0.3, 0.2, 0.1])

    print(f"{collection_name1}:")
    response = client.search(collection_name1, query)
    show(response)

    print(f"{collection_name2}:")
    response = client.search(collection_name2, query)
    show(response)

    response = client.update_alias(collection_name1, alias_name)
    print("set alias")

    response = client.search(alias_name, query)
    show(response)

    response = client.switch_alias(collection_name2, alias_name)
    print("switch alias")
    
    response = client.search(alias_name, query)
    show(response)

    _ = client.delete_index(collection_name1)
    print(f"'{collection_name1}' is deleted.")

    _ = client.delete_index(collection_name2)
    print(f"'{collection_name2}' is deleted.")

    print("DONE")


if __name__ == "__main__":
    main()
