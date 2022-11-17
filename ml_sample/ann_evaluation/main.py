import gc

import numpy as np

from ann import Flat, HNSW
from config import ANNConfig
from evaluate import accuracy_at_k, precision_at_k, recall_at_k, f_measure_at_k, mrr_at_k, map_at_k
from utils import get_data, get_label


def show(y_trues: np.ndarray, y_preds: np.ndarray, k: int=10):
    #accuracy = accuracy_at_k(y_trues, y_preds, k=k)
    precision = precision_at_k(y_trues, y_preds, k=k)
    recall = recall_at_k(y_trues, y_preds, k=k)
    f_measure = f_measure_at_k(y_trues, y_preds, k=k)
    mrr = mrr_at_k(y_trues, y_preds, k=k)
    map_ = map_at_k(y_trues, y_preds, k=k)
    #print(f"accuracy@{k}  : {accuracy}")
    print(f"precision@{k} : {precision}")
    print(f"recall@{k}    : {recall}")
    print(f"f_measure@{k} : {f_measure}")
    print(f"mrr@{k}       : {mrr}")
    print(f"map@{k}       : {map_}")


def main():
    #n_train = 100_000_000
    #n_test = 10_000
    n_train = 100_000
    n_test = 1000
    k = 25
    config = ANNConfig()

    X_train = get_data(n_train, config.n_dimensions)
    X_test = get_data(n_test, config.n_dimensions)
    
    l2 = Flat(config.n_dimensions, config.metric_type)
    y_test = get_label(X_train, X_test, l2, top_n=k)
    del l2
    gc.collect()

    hnsw = HNSW(**config.to_dict())
    hnsw.add(X_train)
    _, y = hnsw.search(X_test, k=k)

    print("[hnsw]")
    show(y_test, y, k=k)

    print("DONE")


if __name__ == "__main__":
    main()
