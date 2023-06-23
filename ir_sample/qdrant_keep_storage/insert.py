from qdrant_client.models import VectorParams

from client import SearchClient
from utils import get_data


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

    print("DONE")


if __name__ == "__main__":
    main()
