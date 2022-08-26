import gc
from time import time

import numpy as np

from recommenders import (
    BaseRecommender,
    FlatIPRecommender,
    FlatL2Recommender,
    HNSWFlatRecommender,
    IVFRecommender,
    PQRecommender,
    LSHRecommender
)
from utils import get_data


def evaluate(recommender: BaseRecommender, x: np.ndarray, n: int=50, verbose: bool=False) -> tuple:
    build_start_tm = time()
    recommender.add(x)
    build_tm = time() - build_start_tm

    search_tms = []
    for i in range(n):
        search_start_tm = time()
        distances, indices = recommender.search(x[i].reshape((1, -1)))
        search_tm = time() - search_start_tm
        search_tms.append(search_tm)

    if verbose:
        print(indices.shape)
        print(distances.shape)
        print(indices)
        print(distances)
        print()

    return build_tm, sum(search_tms)/n


def main():
    n = 10000
    d = 768
    n_nn = 64
    n_bits = 128
    n_subquantizers = int(d / 2)
    
    x = get_data(n, d)

    ip_recommender = FlatIPRecommender(d)
    build_tm, search_tm = evaluate(ip_recommender, x)
    print(f"flat ip: build_tm={build_tm}, average search_tm={search_tm}")
    del ip_recommender
    gc.collect()
    
    l2_recommender = FlatL2Recommender(d)
    build_tm, search_tm = evaluate(l2_recommender, x)
    print(f"flat l2: build_tm={build_tm}, average search_tm={search_tm}")
    del l2_recommender
    gc.collect()
    
    hnsw_recommender = HNSWFlatRecommender(d, n_nn)
    build_tm, search_tm = evaluate(hnsw_recommender, x)
    print(f"flat hnsw: build_tm={build_tm}, average search_tm={search_tm}")
    del hnsw_recommender
    gc.collect()

    ivf_recommender = IVFRecommender(d, n_nn, n_bits)
    build_tm, search_tm = evaluate(ivf_recommender, x)
    print(f"ivf: build_tm={build_tm}, average search_tm={search_tm}")
    del ivf_recommender
    gc.collect()

    pq_recommender = PQRecommender(d, n_subquantizers, n_bits)
    build_tm, search_tm = evaluate(pq_recommender, x)
    print(f"pq: build_tm={build_tm}, average search_tm={search_tm}")
    del pq_recommender
    gc.collect()

    lsh_recommender = LSHRecommender(d, n_bits)
    build_tm, search_tm = evaluate(lsh_recommender, x)
    print(f"lsh: build_tm={build_tm}, average search_tm={search_tm}")
    del lsh_recommender
    gc.collect()

    print("DONE")


if __name__ == "__main__":
    main()
