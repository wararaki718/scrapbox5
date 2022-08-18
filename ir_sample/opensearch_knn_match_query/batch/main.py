import gc
from pathlib import Path
from time import sleep

from client import OpenSearchClient
from config import ClientConfig
from loader import NewsLoader
from mappings import MappingsLoader
from preprocessor import NewsPreprocessor
from query import QueryBuilder
from utils import show
from vectorizer import KeywordVectorizer, NewsVectorizer


def main():
    index_name = "sample-knn-match-index"
    client = OpenSearchClient(ClientConfig.load())

    print("load news:")
    news = NewsLoader.load(Path("data/fakenews.csv"))[:1000]
    print(f"the number of data: {len(news)}")
    print()

    print("vectorize:")
    model_name = "cl-tohoku/bert-base-japanese-v2"
    vectorizer = NewsVectorizer(model_name)
    preprocessor = NewsPreprocessor(vectorizer)
    news = preprocessor.transform(news)
    print(f"vector {len(news[0].vector)}-dim")
    print()
    del vectorizer
    gc.collect()

    print("create index:")
    mappings = MappingsLoader.load(Path("json/mappings.json"))
    response = client.create_index(index_name, mappings)
    print(response)
    print()
    sleep(2)

    print("bulk insert:")
    response = client.bulk_insert(index_name, news)
    print(response)
    print()
    sleep(5)

    print("search results:")
    keyword = "東京"
    vectorizer = KeywordVectorizer(model_name)
    vector = vectorizer.transform(keyword)

    print("# keyword search:")
    query = QueryBuilder.build(keyword=keyword)
    response = client.search(index_name, query)
    show(keyword, response["hits"]["hits"])

    print("# knn search:")
    query = QueryBuilder.build(vector=vector)
    response = client.search(index_name, query)
    show(keyword, response["hits"]["hits"])

    print("# keyword+knn search:")
    query = QueryBuilder.build(keyword=keyword, vector=vector)
    response = client.search(index_name, query)
    show(keyword, response["hits"]["hits"])

    print("delete index:")
    response = client.delete_index(index_name)
    print(response)
    print("DONE")


if __name__ == "__main__":
    main()
