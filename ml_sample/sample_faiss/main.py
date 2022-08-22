import faiss
import numpy as np


def get_data(d: int, n: int = 10000, m: int=1000) -> tuple:
    xb = np.random.random((n, d)).astype(np.float32)
    xb[:, 0] += np.arange(n) / 1000
    xq = np.random.random((n, d)).astype(np.float32)
    xq[:, 0] += np.arange(n) / 1000
    return xb, xq


def main():
    d = 64
    xb, xq = get_data(d)

    print("build:")
    index = faiss.IndexFlatL2(d)
    print(index.is_trained)
    index.add(xb)
    print(index.ntotal)
    print()

    print("search")
    k = 4
    D, I = index.search(xb[:5], k)
    print(I)
    print(D)
    D, I = index.search(xq, k)
    print(I[:5])
    print(I[-5:])
    print()

    print("DONE")


if __name__ == "__main__":
    main()
