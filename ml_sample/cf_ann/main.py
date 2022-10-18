from implicit.datasets.movielens import get_movielens

from ann import UserAnn
from vectorizer import UserVectorizer


def main():
    _, ratings = get_movielens("100k")
    print(ratings.shape)

    vectorizer = UserVectorizer()
    user_factors = vectorizer.fit_transform(ratings)
    print("# embeddings")
    print(f"user: {user_factors.shape}")
    print()

    # build index
    model = UserAnn(dim=user_factors.shape[1])
    model.add(user_factors)

    print("# search")
    distances, indices = model.search(user_factors[0].reshape(1, -1), k=5+1)
    for distance, index in zip(distances[0][1:], indices[0][1:]):
        print(f"{index}: {distance}")
    print()

    print("DONE")


if __name__ == "__main__":
    main()
