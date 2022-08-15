from pathlib import Path
from time import sleep

from client import OpenSearchClient
from config import ClientConfig
from loader import NewsLoader
from mappings import MappingsLoader
from query import QueryBuilder
from utils import show


def main():
    index_name = "sample-kuromoji-index"
    client = OpenSearchClient(ClientConfig.load())

    print("load news:")
    news = NewsLoader.load(Path("data/fakenews.csv"))
    print(f"the number of data: {len(news)}")
    print()

    print("create index:")
    mappings = MappingsLoader.load(Path("json/mappings.json"))
    response = client.create_index(index_name, mappings)
    print(response)
    print()
    sleep(2)

    print("bulk insert:")
    response = client.bulk_insert(index_name, news)
    print(f"errors: {response['errors']}")
    print()
    sleep(5)

    print("kuromoji search:")
    keyword = "東京タワー"
    query = QueryBuilder.build(keyword)
    response = client.search(index_name, query)
    show(keyword, response["hits"]["hits"])
    print()

    print("kuromoji analyze:")
    text = "今日は、東京タワーに行きます。"
    response = client.analyze(index_name, text)
    print(response)
    print()

    print("delete index:")
    response = client.delete_index(index_name)
    print(response)
    print("DONE")


if __name__ == "__main__":
    main()
