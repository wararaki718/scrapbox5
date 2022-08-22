import nmslib
import numpy as np


def main():
    data = np.random.randn(10000, 100).astype(np.float32)

    index = nmslib.init(method="hnsw", space="cosinesimil")
    index.addDataPointBatch(data)
    index.createIndex({"post": 2}, print_progress=True)

    ids, distances = index.knnQuery(data[0], k=10)

    neighbours = index.knnQueryBatch(data, k=10, num_threads=4)
    print(len(neighbours))
    print()
    print("DONE")


if __name__ == "__main__":
    main()
