from torchvision.transforms import Compose, Resize, ToTensor


class TransformerFactory:
    @classmethod
    def create(cls) -> Compose:
        return Compose([
            Resize((100, 100)),
            ToTensor()
        ])
