from pathlib import Path
from time import sleep

from client import OpenSearchClient
from config import ClientConfig
from mappings import MappingsLoader
from query import QueryBuilder
from utils import generate_data, show


def main():
    index_name = "sample-knn-index"
    client = OpenSearchClient(ClientConfig.load())

    print("create index:")
    mappings = MappingsLoader.load(Path("json/mappings.json"))
    response = client.create_index(index_name, mappings)
    print(response)
    print()
    sleep(2)

    print("bulk insert:")
    items = generate_data()
    response = client.bulk_insert(index_name, items)
    print(response)
    print()
    sleep(2)

    print("knn search:")
    query = QueryBuilder.build()

    print(f"query={query}")
    print()

    response = client.search(index_name, query)
    show(response["hits"]["hits"])
    print()
    sleep(2)

    print("delete index:")
    response = client.delete_index(index_name)
    print(response)
    print("DONE")


if __name__ == "__main__":
    main()
