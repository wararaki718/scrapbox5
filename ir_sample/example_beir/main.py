import logging
import random
from pathlib import Path

from beir import util, LoggingHandler
from beir.retrieval.models import SentenceBERT
from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.evaluation import EvaluateRetrieval
from beir.retrieval.search.lexical import BM25Search
from beir.retrieval.search.dense import DenseRetrievalExactSearch


logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    handlers=[LoggingHandler()]
)


def lexical():
    url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/scifact.zip"
    output_path = Path("./data")
    data_path = util.download_and_unzip(url, str(output_path))

    corpus, queries, query_relations = GenericDataLoader(data_path).load(split="test")

    index_name = "scifact"
    model = BM25Search(index_name = index_name)

    retriever = EvaluateRetrieval(model)
    results = retriever.retrieve(corpus, queries)

    measures = retriever.evaluate(query_relations, results, retriever.k_values)
    # logging.info(f"evaluate: {measures}\n")

    query_id, scores_dict = random.choice(list(results.items()))
    logging.info(f"Query: {queries[query_id]}\n")

    scores = sorted(scores_dict.items(), key=lambda item: item[1], reverse=True)
    for rank, score in enumerate(scores[:10], start=1):
        doc_id = score[0]
        logging.info(f"Doc {rank}: {doc_id} [{corpus[doc_id].get('title')}] - {corpus[doc_id].get('text')}\n")


def dense():
    url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/trec-covid.zip"
    output_path = Path("./data")
    data_path = util.download_and_unzip(url, str(output_path))

    corpus, queries, query_relations = GenericDataLoader(data_path).load(split="test")
    
    model_path = "msmarco-distilbert-base-tas-b"
    model = DenseRetrievalExactSearch(SentenceBERT(model_path), batch_size=256, corpus_chunk_size=512*9999)
    
    retriever = EvaluateRetrieval(model, score_function="dot")
    results = retriever.retrieve(corpus, queries)

    measures = retriever.evaluate(query_relations, results, retriever.k_values)
    # logging.info(f"evaluate: {measures}\n")

    mrr = retriever.evaluate_custom(query_relations, results, retriever.k_values, metric="mrr")
    recall_cap = retriever.evaluate_custom(query_relations, results, retriever.k_values, metric="r_cap")
    hole = retriever.evaluate_custom(query_relations, results, retriever.k_values, metric="hole")

    query_id, scores_dict = random.choice(list(results.items()))
    logging.info(f"Query: {queries[query_id]}\n")

    scores = sorted(scores_dict.items(), key=lambda item: item[1], reverse=True)
    for rank, score in enumerate(scores[:10], start=1):
        doc_id = score[0]
        logging.info(f"Doc {rank}: {doc_id} [{corpus[doc_id].get('title')}] - {corpus[doc_id].get('text')}\n")


def main():
    lexical()
    dense()
    logging.info("DONE\n")


if __name__ == "__main__":
    main()
