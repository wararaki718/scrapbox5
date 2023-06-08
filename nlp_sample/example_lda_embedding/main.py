from typing import List

import pandas as pd

from vectorizer import LDAVectorizer


def main() -> None:
    filepath = "data/JP_train.tsv"
    df = pd.read_csv(filepath, sep="\t")
    sentences: List[str] = df["sentence"].dropna().tolist()
    print(sentences[:3])
    print(len(sentences))

    vectorizer = LDAVectorizer()
    x = vectorizer.fit_transform(sentences)
    print(x.shape)
    print("DONE")


if __name__ == "__main__":
    main()
