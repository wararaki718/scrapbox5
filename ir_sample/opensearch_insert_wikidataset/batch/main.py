import gc
from pathlib import Path
from time import sleep

from config import ClientConfig, SearchConfig, TrainConfig
from client import OpenSearchClient
from model import Document
from loader import load_wiki
from preprocessor import Preprocessor
from query import QueryBuilder
from utils import show
from vectorizer import BertVectorizer


def main():
    df = load_wiki().sample(n=300)
    print(df.shape)

    preprocessor = Preprocessor()
    df = preprocessor.transform(df)

    model_name = "cl-tohoku/bert-base-japanese-v2"
    vectorizer = BertVectorizer(model_name)
    df["vector"] = vectorizer.transform(df.text.tolist())
    
    docs = [Document(**document) for document in df.to_dict(orient="records")]
    del df
    gc.collect()

    client = OpenSearchClient(ClientConfig.load())
    config = SearchConfig.load(index_body_path=Path("json/mappings.json"))

    #response = client.delete_index(config.index_name)
    #response = client.delete_model(train_config.model_name)

    print("create_index:")
    response = client.create_index(config.index_name, config.index_body)
    print(f"acknowledged: {response['acknowledged']}")
    print()
    sleep(2)

    print("insert document:")
    response = client.insert(config.index_name, docs[0])
    print(f"successful: {response['_shards']['successful']}")
    print()
    sleep(2)

    print("bulk insert:")
    response = client.bulk_insert(config.index_name, docs[1:])
    print(f"errors: {response['errors']}, items: {len(response['items'])}")
    print()
    sleep(10)

    train_config = TrainConfig.load("sample-model", Path("json/train.json"))
    print("train:")
    response = client.train(train_config.model_name, train_config.model_params)
    print(response)
    print()
    sleep(2)

    print("model status:")
    status = "training"
    while status == "training":
        response = client.get_model_status(train_config.model_name)
        status = response["state"]
        print(status)
        sleep(2)
    print()

    print("delete index:")
    response = client.delete_index(config.index_name)
    print(response)
    print()
    sleep(2)

    print("## knn search")
    config = SearchConfig.load(index_name="knn-sample-index", index_body_path=Path("json/knn_mappings.json"))
    
    print("create_index:")
    response = client.create_index(config.index_name, config.index_body)
    print(f"acknowledged: {response['acknowledged']}")
    print()
    sleep(2)

    print("bulk insert:")
    response = client.bulk_insert(config.index_name, docs)
    print(f"errors: {response['errors']}, items: {len(response['items'])}")
    print()
    sleep(10)

    keyword = "ゲーム"
    print(f"search: keyword={keyword}")

    print("search default:")
    query = QueryBuilder.build(Path("json/query.json"), keyword)
    response = client.search(config.index_name, query)
    show(response["hits"]["hits"])
    print()

    #print("search knn:")
    #query = QueryBuilder.build(Path("json/knn_query.json"), keyword, vectorizer)
    #response = client.search(config.index_name, query)
    #show(response["hits"]["hits"])
    #print()

    print("delete index:")
    response = client.delete_index(config.index_name)
    print(response)
    print()
    sleep(2)

    print("delete model:")
    response = client.delete_model(train_config.model_name)
    print(response)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
