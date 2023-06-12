from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient


def main() -> None:
    collection_name = "texts"
    embeddings = OpenAIEmbeddings()
    texts = [
        "I like to eat apples",
        "I like to eat oranges",
        "I like to eat bananas",
        "I like to eat pears",
    ]

    qdrant = Qdrant.from_texts(
        texts, embeddings,
        location=":memory:",
        collection_name=collection_name,
    )
    print("client created.")

    query = "I like to eat apples"
    results = qdrant.similarity_search(query, top_k=2)
    for result in results:
        print(result.page_content)
    print("DONE")


if __name__ == "__main__":
    main()
