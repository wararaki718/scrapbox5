import numpy as np

from pq import PQ


def main():
    n = 1000
    d = 128
    x_train = np.random.random((n, d))
    x = np.random.random((n, d))
    x_test = np.random.random(d)

    pq = PQ(16, 4)
    pq.fit(x_train)
    codes = pq.encode(x)
    results = pq.search(codes, x_test)
    print(results.shape)
    print(results[:20])
    print("DONE")


if __name__ == "__main__":
    main()
