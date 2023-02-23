from pathlib import Path
from time import sleep

from loaders import BulkLoader, MappingLoader
from search import QueryBuilder, ElasticsearchClient


def show(response: dict):
    buckets = response["aggregations"]["keywords"]["buckets"]
    for bucket in buckets:
        print(f"{bucket['key']}: {bucket['doc_count']}")
    print()


def main():
    hosts = ["http://localhost:9200"]
    index_name = "my_suggest"
    client = ElasticsearchClient(hosts)
    
    print("create index:")
    mapping = MappingLoader.load(Path("json/mapping.json"))
    response = client.create_index(index_name, mapping)
    print(response["result"])
    sleep(2)
    print()

    print("insert data:")
    items = BulkLoader.load(Path("json/bulk.jsonl"))
    response = client.bulk(items)
    print(response)
    sleep(2)
    print()

    print("search:")
    keywords = ["日本", "にほｎ", "にhん", "にっほん", "日本ん"]
    for keyword in keywords:
        query = QueryBuilder.build(keyword)
        response = client.search(index_name, query)
        print(f"search: [{keyword}]")
        show(response)
        sleep(2)

    print("DONE")


if __name__ == "__main__":
    main()
