from time import sleep

from qdrant_client import QdrantClient
from qdrant_client import models

from utils import get_data, get_vector, show


def main():
    collection_name = "sample"
    n = 3000
    dim = 128

    client = QdrantClient(host="localhost", port=6333)
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=dim, distance="Cosine")
    )
    print("get data & vector.")
    data = get_data(n)
    vectors = get_vector(n, dim)

    print("indexing.")
    response = client.upload_collection(
        collection_name=collection_name,
        vectors=vectors,
        payload=data,
        ids=None,
        batch_size=256
    )
    print(response)
    sleep(10)

    print("search.")
    results = client.search(
        collection_name=collection_name,
        query_vector=vectors[0],
        limit=5
    )
    show(results)

    print("DONE")


if __name__ == "__main__":
    main()
