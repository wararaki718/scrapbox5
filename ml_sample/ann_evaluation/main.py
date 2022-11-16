import gc

from ann import Flat, HNSW
from config import ANNConfig
from evaluate import accuracy_at_n
from utils import get_data, get_label


def main():
    #n_train = 100_000_000
    #n_test = 10_000
    n_train = 10_000
    n_test = 100
    config = ANNConfig()

    X_train = get_data(n_train, config.n_dimensions)
    X_test = get_data(n_test, config.n_dimensions)
    
    l2 = Flat(config.n_dimensions, config.metric_type)
    y_test = get_label(X_train, X_test, l2, top_n=1)
    del l2
    gc.collect()

    hnsw = HNSW(**config.to_dict())
    hnsw.add(X_train)
    _, y = hnsw.search(X_test, k=1)

    accuracy = accuracy_at_n(y_test, y, at_n=1)
    print(f"hnsw accuracy: {accuracy}")

    print("DONE")


if __name__ == "__main__":
    main()
