from time import sleep

from qdrant_client.models import VectorParams

from builder import QueryBuilder
from client import SearchClient
from utils import get_data, show


def main():
    collection_name = "sample"

    client = SearchClient()
    
    # prefilter
    query = QueryBuilder.build(key="city", value="London", vector=[0.9, 0.1, 0.1])
    response = client.search(collection_name, query)
    show(response)

    print("DONE")


if __name__ == "__main__":
    main()
