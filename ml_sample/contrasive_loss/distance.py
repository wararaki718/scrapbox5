import torch


def euclidean_distance(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    return (x - y).pow(2).sum().sqrt()

def l1_distance(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    return (x - y).abs().sum()


if __name__ == "__main__":
    a = torch.tensor([[1, 2, 3, 4], [3, 4, 5, 6], [6, 7, 8, 9]])
    c = torch.tensor([[1, 2, 3, 4], [3, 4, 5, 6], [6, 7, 8, 9]])
    b = torch.tensor([[3, 4, 5, 6], [1, 2, 3, 4], [6, 7, 8, 9]])
    print(euclidean_distance(a, b))
    print(euclidean_distance(a, c))
    print(l1_distance(a, b))
    print(l1_distance(a, c))
    result = l1_distance(a, b) * euclidean_distance(a, b)
    print(result)
    print(a.max(1).values)
    print(torch.max(a, dim=1))
