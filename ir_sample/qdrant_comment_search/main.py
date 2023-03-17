from pathlib import Path
from time import sleep

from qdrant_client.models import VectorParams

from builder import QueryBuilder
from client import SearchClient
from config import ModelConfig
from loader import BatchLoader
from preprocessor import BatchPreprocessor
from reader import SentenceReader
from vectorizer import BertVectorizer


def main():
    collection_name = "sample"
    dim = 768

    client = SearchClient()
    params = VectorParams(size=dim, distance="Cosine")
    _ = client.create_index(collection_name, params)
    print(f"index created: {collection_name}")
    sleep(1)

    filepath = Path("data/JP_train.tsv")
    reader = SentenceReader()
    sentences = reader.read(filepath)

    config = ModelConfig.load()
    vectorizer = BertVectorizer(config)
    loader = BatchLoader()
    preprocessor = BatchPreprocessor()
    for batch in loader.load(sentences):
        vectors = vectorizer.transform(batch)
        points = preprocessor.transform(batch, vectors)
        client.insert(collection_name, points)
        print(f"data inserted: {len(points.ids)}")
        sleep(1)

    query = QueryBuilder.build(key="sentence", value="円", vector=vectors[0])
    response = client.search(collection_name, query)
    print(response)
    sleep(1)

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
