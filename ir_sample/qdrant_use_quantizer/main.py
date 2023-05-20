from pathlib import Path

from qdrant_client.models import VectorParams, Distance, ScalarQuantizationConfig, ScalarType

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
    vector_config = VectorParams(size=dim, distance=Distance.COSINE)
    quantization_config = ScalarQuantizationConfig(
        type=ScalarType.INT8,
        quantile=0.99,
        always_ram=True
    )
    _ = client.create_index(collection_name, vector_config, quantization_config)
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

    query = QueryBuilder.build(key="sentence", text="is", vector=vectors[0])
    response = client.search(collection_name, query)
    show(response)

    _ = client.delete_index(collection_name)
    print(f"index deleted: {collection_name}")

    print("DONE")


if __name__ == "__main__":
    main()
