import gc
import os

from hnsw_flat import HNSWFlatRecommender
from utils import get_data

def main():
    n = 1000
    d = 128
    n_nn = 64
    filename = "hnsw_index.pkl"
    
    x = get_data(n, d)

    recommender = HNSWFlatRecommender(d, n_nn)
    recommender.add(x)

    distances, indices = recommender.search(x[0].reshape((1, -1)))
    print(distances)
    print(indices)
    print()

    recommender.write(filename)
    del recommender
    gc.collect()

    recommender = HNSWFlatRecommender(d, n_nn)
    recommender.read(filename)

    distances, indices = recommender.search(x[0].reshape((1, -1)))
    print(distances)
    print(indices)
    print()

    print(os.listdir("."))
    os.remove(filename)
    print(os.listdir("."))

    print("DONE")


if __name__ == "__main__":
    main()
