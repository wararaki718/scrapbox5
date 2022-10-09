from sklearn.feature_extraction.text import HashingVectorizer


def main():
    corpus = [
        "this is a pen",
        "this is an apple",
        "there is a pen",
        "that is a book",
        "there are books",
        "i have an apple"
    ]
    vectorizer = HashingVectorizer(n_features=len(corpus))
    X = vectorizer.fit_transform(corpus)
    print(X.shape)
    print(X.toarray())
    print("DONE")


if __name__ == "__main__":
    main()
