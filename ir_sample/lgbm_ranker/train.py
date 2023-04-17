import torch
from lightgbm import LGBMRanker
from pytorchltr.datasets.svmrank.svmrank import SVMRankDataset


class Trainer:
    def __init__(self):
        pass

    def train(self,
              model: LGBMRanker,
              dataset: SVMRankDataset,
              epochs: int=3,
              learning_rate: float=0.1) -> LGBMRanker:


        loader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=dataset.collate_fn())
        for batch in loader:
            xs = batch.features
            ys = batch.relevance
            n = batch.n

        return model
