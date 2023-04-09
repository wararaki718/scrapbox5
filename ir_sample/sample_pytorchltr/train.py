import torch
from pytorchltr.datasets.svmrank.svmrank import SVMRankDataset
from pytorchltr.loss import PairwiseHingeLoss

from model import NNModel


class Trainer:
    def __init__(self):
        pass

    def train(self,
              model: NNModel,
              dataset: SVMRankDataset,
              epochs: int=3,
              learning_rate: float=0.1) -> NNModel:
        model.train()
        optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
        criterion = PairwiseHingeLoss()
        for _ in range(epochs):
            loader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=dataset.collate_fn())
            for batch in loader:
                xs = batch.features
                ys = batch.relevance
                n = batch.n
                loss = criterion(model(xs), ys, n).mean()
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        return model
