import gc
import json
from pathlib import Path
from time import sleep

from config import ClientConfig, SearchConfig
from client import OpenSearchClient
from model import Document
from loader import load_wiki
from preprocessor import Preprocessor
from vectorizer import BertVectorizer


def main():
    df = load_wiki().head(300)
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

    response = client.delete_index(config.index_name)

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
    response = client.bulk_insert(config.index_name, docs[1:10])
    print(f"errors: {response['errors']}, items: {len(response['items'])}")
    print()
    sleep(2)

    print("search:")
    response = client.search(config.index_name)
    print(f"number of hits: {len(response['hits'])}")
    print()
    sleep(2)

    print("train:")
    with open("json/train.json") as f:
        train_body = json.load(f)
    response = client.train(train_body)
    print(response)
    print()
    sleep(2)

    print("model status:")
    response = client.model_status()
    print(response)
    print()
    sleep(2)
    
    print("delete index:")
    response = client.delete_index(config.index_name)
    print(response)
    print()

    print("delete model:")
    response = client.delete_model()
    print(response)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
