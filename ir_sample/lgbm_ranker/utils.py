import gc
from typing import Optional, Tuple, List

import numpy as np
import scipy.sparse as sps
from torch.utils.data import DataLoader
from pytorchltr.datasets.svmrank.svmrank import SVMRankDataset


def create_dataset(dataset: SVMRankDataset, n_sample: Optional[int] = None) -> Tuple[sps.csr_matrix, np.ndarray, List[int]]:
    loader = DataLoader(
        dataset,
        batch_size=1,
        shuffle=True,
        collate_fn=dataset.collate_fn()
    )

    X = []
    y = []
    qids = []
    for batch in loader:
        X.append(batch.features.cpu().detach().numpy()[0])
        y.append(batch.relevance.cpu().detach().numpy()[0])
        qids.append(batch.n[0].item())
    
    if n_sample is not None:
        picks = np.random.choice(len(X), n_sample, replace=False)
        X_new = []
        y_new = []
        qids_new = []
        for pick in picks:
            X_new.append(X[pick])
            y_new.append(y[pick])
            qids_new.append(qids[pick])
        X = X_new
        y = y_new
        qids = qids_new
        gc.collect()
    
    del loader
    gc.collect()
    
    X = sps.csr_matrix(np.vstack(X))
    # X = np.vstack(X)[:, :2]
    y = np.hstack(y).flatten()

    return X, y, qids
