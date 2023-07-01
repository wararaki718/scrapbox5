import logging

from torch.optim.optimizer import Optimizer
from torch.utils.data import DataLoader

from criterion import ContrasiveLoss
from model import SiameseNetwork


logger = logging.getLogger(__name__)


class Trainer:
    def __init__(self) -> None:
        pass

    def train(
        self,
        model: SiameseNetwork,
        loader: DataLoader,
        criterion: ContrasiveLoss,
        optimizer: Optimizer,
        epochs: int=100
    ) -> None:
        n_iteration = 0

        for epoch in range(1, epochs+1):
            for i, (img0, img1, label) in enumerate(loader):
                img0 = img0.cuda()
                img1 = img1.cuda()
                label = label.cuda()
                
                optimizer.zero_grad()
                output1, output2 = model(img0, img1)
                loss = criterion(output1, output2, label)
                
                loss.backward()
                optimizer.step()

                if i % 10 == 0 :
                    logger.info(f"Epoch number {epoch}: Current loss {loss.item()}")
                    n_iteration += 10
