import torch
import torch.nn as nn
import torchvision


class SiameseNetwork(nn.Module):
    def __init__(self) -> None:
        super(SiameseNetwork, self).__init__()

        self.resnet = torchvision.models.resnet18(weights=None)

        self.resnet.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
        self.fc_in_features = self.resnet.fc.in_features

        self.resnet = nn.Sequential(*(list(self.resnet.children())[:-1]))

        self.fc = nn.Sequential(
            nn.Linear(self.fc_in_features * 2, 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 1)
        )

        self.sigmoid = nn.Sigmoid()
    
    def _init_weights(self, m: nn.Module) -> None:
        if isinstance(m, nn.Linear):
            nn.init.xavier_uniform_(m.weight)
            m.bias.data.fill_(0.01)

    def forward_once(self, x: torch.Tensor) -> torch.Tensor:
        output = self.resnet(x)
        output = output.view(output.size()[0], -1)
        return output

    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
        x1 = self.forward_once(x1)
        x2 = self.forward_once(x2)

        x = torch.cat((x1, x2), 1)
        x = self.fc(x)
        x = self.sigmoid(x)

        return x
