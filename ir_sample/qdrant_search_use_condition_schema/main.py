from pathlib import Path

from qdrant_client.models import VectorParams, TextIndexParams, TokenizerType, TextIndexType, Distance

from loader import BatchLoader
from preprocessor import BatchPreprocessor
from reader import SentenceReader
from schema.condition import Condition
from search.builder import QueryBuilder
from search.client import SearchClient
from utils import show
from vectorizer import RandomVectorizer


def main():
    collection_name = "sample"
    dim = 256

    client = SearchClient()
    params = VectorParams(size=dim, distance=Distance.COSINE)
    _ = client.create_index(collection_name, params)
    print(f"index created: {collection_name}")

    filepath = Path("data/EN-ext_train.tsv")
    reader = SentenceReader()
    sentences = reader.read(filepath)
    print(len(sentences))

    vectorizer = RandomVectorizer()
    loader = BatchLoader()
    preprocessor = BatchPreprocessor()
    vectors = []
    for i, batch in enumerate(loader.load(sentences, batch_size=1024)):
        vectors = vectorizer.generate(len(batch), dim)
        points = preprocessor.transform(batch, vectors)
        client.insert(collection_name, points)
        print(f"{i}-th data inserted: {len(points.ids)}")
    print()
    
    params = TextIndexParams(
        type=TextIndexType.TEXT,
        tokenizer=TokenizerType.WHITESPACE,
        min_token_len=2,
        max_token_len=15,
        lowercase=True
    )
    field_name = "sentence"
    client.create_payload_index(collection_name, field_name, params)

    condition = Condition(
        key="is",
        category="A",
        price_lower=1000,
        price_upper=4000,
    )

    query = QueryBuilder.build(condition, vector=vectors[0])
    response = client.search(collection_name, query)
    print(condition)
    show(response)

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
