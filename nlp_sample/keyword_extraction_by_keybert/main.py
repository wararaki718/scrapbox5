from keybert import KeyBERT

from utils import get_doc


def show(results: list):
    for result in results:
        print(f"{result[0]}: {result[1]}")
    print()


def main():
    doc = get_doc()

    model = KeyBERT()
    results = model.extract_keywords(doc)
    show(results)

    results = model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None)
    show(results)
    
    results = model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None)
    show(results)

    results = model.extract_keywords(doc, keyphrase_ngram_range=(3, 3), stop_words="english", use_maxsum=True, nr_candidates=20, top_n=5)
    show(results)

    results = model.extract_keywords(doc, keyphrase_ngram_range=(3, 3), stop_words="english", use_mmr=True, diversity=0.7)
    show(results)

    print("DONE")


if __name__ == "__main__":
    main()
