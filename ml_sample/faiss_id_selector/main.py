import random
from pathlib import Path

import faiss
import numpy as np

from loader import load_pokemon
from preprocessor import PokemonPreprocessor
from utils import show, show_status
from vectorizer import PokemonVectorizer


def main():
    df = load_pokemon(Path("data/Pokemon.csv"))
    print(df.shape)

    preprocessor = PokemonPreprocessor()
    names, features = preprocessor.transform(df)

    vectorizer = PokemonVectorizer()
    X = vectorizer.transform(features)

    #ids = np.array(list(range(X.shape[0])))
    #xids = np.ascontiguousarray(ids, dtype=np.int64)
    hnsw = faiss.IndexHNSWFlat(X.shape[1], 24)
    hnsw.add(X)
    #hnsw.add_with_ids(X, xids)
    show_status(hnsw)

    index = random.randint(0, len(names)-1)
    query = X[index].reshape((1, -1))
    distances, indices = hnsw.search(query, 11)
    show(names, index, distances[0], indices[0])

    # a = np.array(list(range(1, 151)))
    # a = np.ascontiguousarray(a, dtype=np.int64)
    # selector = faiss.IDSelectorBatch(n=a.shape[0], indices=a)
    # distances, indices = hnsw.search(query, 11, sel=selector)
    # show(names, index, distances[0], indices[0])

    print("DONE")


if __name__ == "__main__":
    main()
