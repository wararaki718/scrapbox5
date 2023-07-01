from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from analyzer import CustomAnalyzer


def main() -> None:
    texts = [
        "machine learning",
        "ai ml machine learning",
        "programming language",
        "python java program",
        "english japanese",
        "program machine learning",
        "ai python data",
        "data java learning",
        "machine is good",
        "learning is good",
        "machine and learning",
        "this is machine"
    ]

    custom_analyzer = CustomAnalyzer()

    count_vectorizer = CountVectorizer(analyzer=custom_analyzer)
    count_vectorizer.fit(texts)

    tfidf_vectorizer = TfidfVectorizer(analyzer=custom_analyzer)
    tfidf_vectorizer.fit(texts)

    names = count_vectorizer.get_feature_names_out()
    vectors = count_vectorizer.transform(texts)
    print(names)
    print(vectors)

    names = tfidf_vectorizer.get_feature_names_out()
    vectors = tfidf_vectorizer.transform(texts)
    idf = tfidf_vectorizer.idf_
    print(names)
    print(idf)
    print(vectors)

    print("DONE")


if __name__ == "__main__":
    main()
