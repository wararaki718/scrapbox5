import torch

from batch import BatchIterator
from model import MLPModel
from utils import try_gpu, random_pairs


class LTRTrainer:
    def __init__(self):
        pass

    def train(self, model: MLPModel, batch_iter: BatchIterator, learning_rate: float=0.001, epochs: int=2) -> MLPModel:
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        for epoch in range(1, 1+epochs):
            total_loss = 0.0
            for i, (X, y, _) in enumerate(batch_iter):
                picks = random_pairs(len(X))

                X1_train = try_gpu(X[picks[0]])
                X2_train = try_gpu(X[picks[1]])

                y1_train = try_gpu(y[picks[0]])
                y2_train = try_gpu(y[picks[1]])

                optimizer.zero_grad()
                y1_preds = model(X1_train)
                y2_preds = model(X2_train)
                loss = torch.margin_ranking_loss(y1_preds, y2_preds, y1_train - y2_train).sum()
                
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
                if i % 100 == 0:
                    print(f"[epoch={epoch}, i={i}] loss: {loss}")
            
            print(f"total_loss={total_loss}")
        
        return model
