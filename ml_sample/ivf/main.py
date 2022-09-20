import numpy as np

from ivf import IVF


def main():
    n = 1000
    d = 128
    x = np.random.random((n, d))
    x_test = np.random.random(d)

    n_clusters = 128
    ivf = IVF(n_clusters)
    ivf.fit(x)
    indices, distances = ivf.search(x_test, k=10)
    print(indices)
    print(distances)
    print("DONE")


if __name__ == "__main__":
    main()
