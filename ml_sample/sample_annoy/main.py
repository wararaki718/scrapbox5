import numpy as np
from annoy import AnnoyIndex


def main():
    n = 1000
    dim = 20
    n_trees = 10

    index = AnnoyIndex(dim, "angular")
    for i in range(n):
        vector = np.random.random(dim)
        index.add_item(i, vector)
    
    i_target = 10
    top_n = 5
    index.build(n_trees)
    results = index.get_nns_by_item(i_target, top_n)
    print(results)

    print("DONE")


if __name__ == "__main__":
    main()
