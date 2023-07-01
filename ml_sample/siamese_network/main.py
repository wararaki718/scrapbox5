import logging

from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets

from dataset import SiameseNetworkDataset
from criterion import ContrasiveLoss
from model import SiameseNetwork
from tester import Tester
from trainer import Trainer
from transform import TransformerFactory


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    images = datasets.ImageFolder(root="./data/faces/training/")
    logger.info("set image folders")

    transformer = TransformerFactory.create()
    dataset = SiameseNetworkDataset(images, transformer)
    train_loader = DataLoader(dataset, shuffle=True, num_workers=8, batch_size=64)
    logger.info("data loader created.")
    
    model = SiameseNetwork().cuda()
    criterion = ContrasiveLoss().cuda()
    optimizer = optim.Adam(model.parameters(), lr=0.0005)
    logger.info("model defined.")

    siamese_trainer = Trainer()
    siamese_trainer.train(model, train_loader, criterion, optimizer)
    logger.info("finish train")

    images = datasets.ImageFolder(root="./data/faces/testing/")
    siamese_dataset = SiameseNetworkDataset(images, transformer)
    test_loader = DataLoader(siamese_dataset, num_workers=2, batch_size=1, shuffle=True)
    logger.info("set test images")

    siamese_tester = Tester()
    siamese_tester.test(model, test_loader)
    logger.info("finish test")
    logger.info("DONE")


if __name__ == "__main__":
    main()
