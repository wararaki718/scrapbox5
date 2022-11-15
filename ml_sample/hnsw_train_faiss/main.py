import gc

from hnsw import HNSW
from utils import get_data


def main():
    n_nn = 16
    dim = 128
    
    x = get_data(n_nn, dim)
    print(f"the number of feature: {x.shape[1]}")
    print()
    
    print("[hnsw.add]")
    hnsw = HNSW(dim, n_nn)
    hnsw.add(x)
    print(f"- train: {hnsw.is_trained}")
    del hnsw
    gc.collect()
    print()

    print("[hnsw.train]")
    hnsw = HNSW(dim, n_nn)
    hnsw.train(x)
    print(f"- train: {hnsw.is_trained}")
    del hnsw
    gc.collect()
    print()

    print("DONE")


if __name__ == "__main__":
    main()