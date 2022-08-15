import gc
from pathlib import Path
from time import sleep

from client import OpenSearchClient
from config import ClientConfig
from loader import NewsLoader
from mappings import MappingsLoader
from query import QueryBuilder
from utils import show
from vectorizer import BertVectorizer


def main():
    index_name = "sample-knn-index"
    client = OpenSearchClient(ClientConfig.load())

    print("load news:")
    news = NewsLoader.load(Path("data/fakenews.csv"))[:31]
    print(f"the number of data: {len(news)}")
    print()

    print("vectorize:")
    model_name = "cl-tohoku/bert-base-japanese-v2"
    vectorizer = BertVectorizer(model_name)
    vectors = vectorizer.transform(news)
    for i in range(len(vectors)):
        news[i].vector = vectors[i].copy()
    print(f"vector {len(vectors[0])}-dim")
    print()
    del vectors, vectorizer
    gc.collect()

    print("create index:")
    mappings = MappingsLoader.load(Path("json/mappings.json"))
    response = client.create_index(index_name, mappings)
    print(response)
    print()
    sleep(2)

    print("bulk insert:")
    response = client.bulk_insert(index_name, news[1:])
    print(response)
    print()
    sleep(5)

    print("knn search:")
    query = QueryBuilder.build(news[0].vector)
    print()

    response = client.search(index_name, query)
    show(news[0], response["hits"]["hits"])
    print()
    sleep(2)

    print("delete index:")
    response = client.delete_index(index_name)
    print(response)
    print("DONE")


if __name__ == "__main__":
    main()
