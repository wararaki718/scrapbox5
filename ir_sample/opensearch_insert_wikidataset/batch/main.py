import gc
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

    client = OpenSearchClient(ClientConfig())
    config = SearchConfig()

    print("create_index:")
    response = client.create_index(config.index_name, config.index_body)
    print(response)
    print()
    sleep(2)

    print("insert document:")
    response = client.insert(config.index_name, docs[0])
    print(response)
    print()
    sleep(2)

    print("bulk insert:")
    response = client.bulk_insert(config.index_name, docs[1:10])
    print(response)
    print()
    sleep(2)

    print("search:")
    response = client.search(config.index_name)
    print(response)
    print()
    sleep(2)
    
    print("delete index:")
    response = client.delete_index(config.index_name)
    print(response)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
