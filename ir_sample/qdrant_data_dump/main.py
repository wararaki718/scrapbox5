from pathlib import Path
from time import sleep

from qdrant_client.models import VectorParams

from builder import QueryBuilder
from client import SearchClient
from utils import get_data


def main():
    collection_name = "sample"
    dim = 3

    client = SearchClient()
    response = client.get_collections()
    print(response)
    sleep(1)

    # exists snapshot
    if len(response.collections) > 0:
        query = QueryBuilder.build(key="city", value="London", vector=[0.3, 0.2, 0.1])
        response = client.search(collection_name, query)
        print(response)
        sleep(1)
        return

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

    response = client.get_collections()
    print(response)
    sleep(1)

    print("create a snapshot")
    snapshot = client.create_snapshot(collection_name)
    print(snapshot)
    sleep(1)

    print("rename snapshot")
    before = Path(f"./snapshots/{collection_name}/{snapshot.name}")
    after = Path(f"./snapshots/{collection_name}/samplefile.snapshot")
    after.unlink(missing_ok=True)
    before.rename(after)
    print(f"before: {before}")
    print(f"after : {after}")

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")
    sleep(1)

    print("DONE")


if __name__ == "__main__":
    main()
