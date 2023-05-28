from qdrant_client.models import VectorParams, TextIndexParams, TokenizerType, TextIndexType, Distance

from builder import QueryBuilder
from client import SearchClient
from loader import BatchLoader
from preprocessor import BatchPreprocessor
from reader import SentenceReader
from utils import show
from vectorizer import RandomVectorizer


def main():
    collection_name = "sample"
    dim = 256

    client = SearchClient()
    params = VectorParams(size=dim, distance=Distance.COSINE)
    _ = client.create_index(collection_name, params)
    print(f"index created: {collection_name}")

    reader = SentenceReader()
    sentences = reader.read()
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
    
    params = TextIndexParams(
        type=TextIndexType.TEXT,
        tokenizer=TokenizerType.WHITESPACE,
        lowercase=True
    )
    field_name = "sentence"
    client.create_payload_index(collection_name, field_name, params)

    ## search test
    query = QueryBuilder.build(key="sentence", text="hello", vector=vectors[0])
    response = client.search(collection_name, query)
    print(query)
    show(response)

    query = QueryBuilder.build(key="sentence", text="hello world", vector=vectors[0])
    response = client.search(collection_name, query)
    print(query)
    show(response)

    query = QueryBuilder.build(key="sentence", text="hello cup", vector=vectors[0])
    response = client.search(collection_name, query)
    print(query)
    show(response)

    query = QueryBuilder.build(key="sentence", text="hello good cup", vector=vectors[0])
    response = client.search(collection_name, query)
    print(query)
    show(response)

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
