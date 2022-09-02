from sklearn.cluster import KMeans

from kmeans import SCKMeans
from utils import get_data


def main():
    n_clusters = 5
    dim = 5
    x_train = get_data(1000, dim)
    x_test = get_data(10, dim)
    print(x_train.shape)
    print(x_test.shape)
    print()

    print("scipy:")
    smodel = SCKMeans(n_clusters=n_clusters, n_iter=300)
    smodel.fit(x_train)
    y = smodel.predict(x_test)
    print(y)
    print()

    print("scikit-learn:")
    model = KMeans(n_clusters=n_clusters)
    model.fit(x_train)
    y = model.predict(x_test)
    print(y)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
