import torch

from model import NNModel


class NNTrainer:
    def __init__(self):
        pass

    def train(self, model: NNModel, X: torch.Tensor, y: torch.Tensor, epochs: int=2, batch_size: int = 32) -> NNModel:
        optimizer = torch.optim.Adam(model.parameters())
        criterion = torch.nn.CrossEntropyLoss()

        for epoch in range(1, 1+epochs):
            total_loss = 0.0
            for i, index in enumerate(range(0, X.shape[0], batch_size)):
                X_train = torch.Tensor(X[index: index+batch_size].toarray())
                y_train = torch.Tensor(y[index: index+batch_size]).to(torch.int64)

                optimizer.zero_grad()
                y_preds = model(X_train)
                loss = criterion(y_preds, y_train)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
                if i % 100 == 0:
                    print(f"[epoch={epoch}, i={i}] loss: {loss}")
            
            print(f"total_loss={total_loss}")
        
        return model
