import torch
from pytorchltr.datasets.svmrank.svmrank import SVMRankDataset
from pytorchltr.evaluation import ndcg

from model import NNModel
from utils import try_gpu


class Evaluator:
    def __init__(self):
        pass

    def evaluate(self, model: NNModel, dataset: SVMRankDataset) -> float:
        model.eval()
        loader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=dataset.collate_fn())

        score = 0.0
        for batch in loader:
            xs = try_gpu(batch.features)
            ys = try_gpu(batch.relevance)
            n = batch.n

            y_preds = model(xs)
            score += ndcg(y_preds, ys, n, k=10).sum().item()
        
        return score / len(dataset)
    