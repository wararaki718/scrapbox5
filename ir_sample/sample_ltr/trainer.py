from typing import Optional

import torch

from batch import BatchIterator
from evaluator import LTREvaluator
from loss import listwise_loss
from model import MLPModel
from utils import try_gpu, convert_gamma_to_implicit


class LTRTrainer:
    def __init__(self):
        self._evaluator = LTREvaluator()

    def train(self,
              model: MLPModel,
              train_iter: BatchIterator,
              valid_iter: Optional[BatchIterator]=None,
              learning_rate: float=0.001,
              epochs: int=2) -> MLPModel:
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        for epoch in range(1, 1+epochs):
            total_loss = 0.0
            model.train()
            for i, (X, y, _) in enumerate(train_iter):
                X_train = try_gpu(X)
                #y_train, theta = convert_gamma_to_implicit(y, pow_true=0.0)
                y_train = try_gpu(y)
                #theta = try_gpu(theta)

                optimizer.zero_grad()
                y_preds = model(X_train)
                loss = listwise_loss(y_preds, y_train)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
                if i % 1000 == 0:
                    print(f"[epoch={epoch}, i={i}] loss: {loss}")
            
            if valid_iter is not None:
                score = self._evaluator.evaluate(model, valid_iter)
                print(f"valid ndcg@5: {score}")

            
            print(f"total_loss={total_loss}")
        
        return model
