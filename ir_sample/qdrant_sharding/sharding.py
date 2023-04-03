import json
from qdrant_client.models import CollectionInfo, Distance, VectorParams

from recreate import SearchClient


def show(info: CollectionInfo):
    data = info.dict()
    print(json.dumps(data, indent=4))
    print()


def main():
    collection_name = "reviews_shard"
    base = "reviews"
    params = VectorParams(
        size=768,
        distance=Distance.COSINE
    )

    # copy parameters (data is not copied)
    client = SearchClient()
    _ = client.recreate_index(collection_name, params, base)

    response = client.get_cluster(base)
    show(response)

    response = client.get_cluster(collection_name)
    show(response)

    print("DONE")


if __name__ == "__main__":
    main()
