import torch
import numpy as np
from lightgbm import Dataset
from pytorchltr.datasets.svmrank.svmrank import SVMRankDataset


def create_dataset(dataset: SVMRankDataset) -> Dataset:
    loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=2,
        shuffle=True,
        collate_fn=dataset.collate_fn()
    )

    X = []
    y = []
    qids = []
    for batch in loader:
        print(batch.features[0])
        print(batch.relevance[0])
        print(batch.n[0])
        print("----")
        X.append(batch.features.cpu().detach().numpy()[0])
        y.append(batch.relevance.cpu().detach().numpy()[0])
        qids.append(batch.n[0])
    X = np.vstack(X)
    y = np.hstack(y)

    print(X.shape)
    print(y.shape)
    print(len(qids))

    return X, y, qids
