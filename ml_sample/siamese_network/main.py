from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets

from dataset import SiameseNetworkDataset
from criterion import ContrasiveLoss
from model import SiameseNetwork
from tester import Tester
from trainer import Trainer
from transform import TransformerFactory


def main() -> None:
    images = datasets.ImageFolder(root="./data/faces/traning/")
    transformer = TransformerFactory.create()

    dataset = SiameseNetworkDataset(images, transformer)
    train_loader = DataLoader(dataset, shuffle=True, num_workers=8, batch_size=64)
    
    model = SiameseNetwork().cuda()
    criterion = ContrasiveLoss().cuda()
    optimizer = optim.Adam(model.parameters(), lr=0.0005)

    siamese_trainer = Trainer()
    siamese_trainer.train(model, train_loader, criterion, optimizer)

    images = datasets.ImageFolder(rott="./data/faces/testing/")
    siamese_dataset = SiameseNetworkDataset(imageFolderDataset=images, transform=transformer)
    test_loader = DataLoader(siamese_dataset, num_workers=2, batch_size=1, shuffle=True)

    siamese_tester = Tester()
    siamese_tester.test(model, test_loader)

    print("DONE")


if __name__ == "__main__":
    main()
