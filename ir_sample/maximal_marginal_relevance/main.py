from mmr import mmr
from ranking import ranking
from utils import get_data


def main():
    n = 100
    dim = 16
    documents = get_data(n, dim)
    query = get_data(1, dim)
    items = ranking(query, documents)
    results = mmr(query, documents, items, lambda_=0.2)
    print("results:")
    print(items[:10])
    print()
    print(results[:10])
    print()

    print("DONE")


if __name__ == "__main__":
    main()
