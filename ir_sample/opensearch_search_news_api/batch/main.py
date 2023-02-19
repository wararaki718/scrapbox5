import gc
from pathlib import Path
from time import sleep

from index import BertVectorizer, OpenSearchClient
from schemas.config import ClientConfig, ModelConfig, SearchConfig
from loaders import MappingsLoader, NewsLoader


def main():
    search_config = SearchConfig.load()
    client = OpenSearchClient(ClientConfig.load())

    print("load news:")
    news = NewsLoader.load(Path("data/fakenews.csv"))[:31]
    print(f"the number of data: {len(news)}")
    print()

    print("vectorize:")
    model_config = ModelConfig()
    vectorizer = BertVectorizer(model_config)
    vectors = vectorizer.transform(news)
    for i in range(len(vectors)):
        news[i].vector = vectors[i].copy()
    print(f"vector {len(vectors[0])}-dim")
    print()
    del vectors, vectorizer
    gc.collect()

    print("create index:")
    mappings = MappingsLoader.load(Path("json/mappings.json"))
    response = client.create_index(search_config.index_name, mappings)
    print(response)
    print()
    sleep(2)

    print("bulk insert:")
    response = client.bulk_insert(search_config.index_name, news[1:])
    print(response)
    print()
    sleep(5)

    print("DONE")


if __name__ == "__main__":
    main()
