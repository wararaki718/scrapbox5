import torch

from loss import ContrasiveLoss


def main() -> None:
    y_true = torch.tensor([0, 1, 0, 1]) # 0 is same, 1 is different
    y_pred = torch.tensor([0.2, 0.9, 0.4, 0.5])
    contrasive_loss = ContrasiveLoss()
    loss = contrasive_loss(y_true, y_pred)
    print(loss)
    print("DONE")


if __name__ == "__main__":
    main()
