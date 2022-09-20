import numpy as np

from pqlsh import PQLSH


def main():
    n = 1000
    d = 128
    x = np.random.random((n, d))
    query = np.random.random(d)

    lsh = PQLSH(64, 4, 128, threshold=0.2)
    lsh.add(x)
    results = lsh.search(query)
    print(results)
    print("DONE")


if __name__ == "__main__":
    main()
