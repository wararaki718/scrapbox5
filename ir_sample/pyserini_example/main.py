import gc

from pyserini.search.faiss import FaissSearcher, TctColBertQueryEncoder
from pyserini.search.hybrid import HybridSearcher
from pyserini.search.lucene import LuceneSearcher, LuceneImpactSearcher


def show(hits: list):
    for i in range(0, 10):
        print(f"{i + 1:2} {hits[i].docid:7} {hits[i].score:.5f}")
    print()


def main():
    query = "what is a lobster roll?"

    # bm25
    print("bm25:")
    searcher = LuceneSearcher.from_prebuilt_index("msmarco-v1-passage")
    hits = searcher.search(q=query)
    show(hits)
    del searcher
    gc.collect()
    
    # sparse
    print("sparse:")
    ssearcher = LuceneImpactSearcher.from_prebuilt_index(
        "msmarco-v1-passage-unicoil",
        "castorini/unicoil-msmarco-passage"
    )
    hits = ssearcher.search(q=query)
    show(hits)

    # dense
    print("dense:")
    encoder = TctColBertQueryEncoder("castorini/tct_colbert-msmarco")
    dsearcher = FaissSearcher.from_prebuilt_index(
        "msmarco-passage-tct_colbert-hnsw",
        encoder
    )
    hits = dsearcher.search(query=query)
    show(hits)
    gc.collect()

    # hybrid
    print("hybrid:")
    hsearcher = HybridSearcher(dsearcher, ssearcher)
    hits = hsearcher.search(query=query)
    show(hits)

    print("DONE")


if __name__ == "__main__":
    main()
