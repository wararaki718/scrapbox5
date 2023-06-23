from pathlib import Path
from time import sleep

from client import ElasticsearchClient
from dataset import DatasetGenerator
from mapping import MappingLoader
from schema.query import Query


def main():
    host = "http://localhost:9200"
    client = ElasticsearchClient(hosts=[host])

    filename = Path("json/mappings.json")
    mappings = MappingLoader.load(filename)

    index_name = "sample"
    client.create_index(index_name=index_name, mappings=mappings)
    print(f"create '{index_name}'!")
    sleep(1)

    total = client.count(index_name)
    print(total)
    print()

    for i, doc in enumerate(DatasetGenerator.generate(), start=1):
        _ = client.insert(index_name, i, doc)
        print(f"inserted ({i})")
        sleep(1)
    print()
    
    total = client.count(index_name)
    print(total)
    print()
    
    results = client.search(index_name)
    print(results["hits"])
    print()

    query = Query(rank_feature="topics.politics")
    results = client.search(index_name, query.to_query())
    print(results["hits"])
    print()

    query = Query(rank_feature="negative_reviews.1star")
    results = client.search(index_name, query.to_query())
    print(results["hits"])
    print()

    client.delete_index(index_name)
    print(f"delete {index_name}")

    print("DONE")


if __name__ == "__main__":
    main()
