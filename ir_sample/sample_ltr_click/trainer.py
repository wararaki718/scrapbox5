import torch

from batch import BatchIterator
from loss import listwise_loss
from model import MLPModel
from utils import try_gpu, convert_gamma_to_implicit


class LTRTrainer:
    def __init__(self):
        pass

    def train(self, model: MLPModel, batch_iter: BatchIterator, learning_rate: float=0.001, epochs: int=2) -> MLPModel:
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        for epoch in range(1, 1+epochs):
            total_loss = 0.0
            for i, (X, y, _) in enumerate(batch_iter):
                X_train = try_gpu(X)
                y_train, theta = convert_gamma_to_implicit(y, pow_true=0.0)
                y_train = try_gpu(y_train)
                theta = try_gpu(theta)

                optimizer.zero_grad()
                y_preds = model(X_train)
                loss = listwise_loss(y_preds, y_train, theta)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
                if i % 100 == 0:
                    print(f"[epoch={epoch}, i={i}] loss: {loss}")
            
            print(f"total_loss={total_loss}")
        
        return model
