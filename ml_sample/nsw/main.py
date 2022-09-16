import numpy as np

from nsw import NSW


def main():
    n = 1000
    dim = 3
    X = np.random.random((n, dim))
    
    print("indexing...", flush=True)
    nsw = NSW(5, 5)
    nsw.add(X)

    print("search", flush=True)
    q = np.random.random(dim)
    result = nsw.get_neighbor(q)
    print("result:")
    print(f"q={q}")
    print(f"neighbor={result.vector}")

    print("DONE")


if __name__ == "__main__":
    main()
