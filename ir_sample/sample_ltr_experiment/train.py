import torch
from pytorchltr.datasets.svmrank.svmrank import SVMRankDataset
from pytorchltr.loss import LambdaNDCGLoss2

from model import NNModel
from utils import try_gpu


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
        criterion = LambdaNDCGLoss2()
        for epoch in range(epochs):
            total_loss = 0.0
            loader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=dataset.collate_fn())
            for batch in loader:
                xs = try_gpu(batch.features)
                ys = try_gpu(batch.relevance)
                n = batch.n
                loss = criterion(model(xs), ys, n).mean()
                total_loss += loss.item()
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            print(f"[epoch {epoch}]: {total_loss}")

        return model
