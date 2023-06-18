import torch.nn as nn
from torch import optim
from torch.utils.data import DataLoader

from utils import try_gpu


class Seq2SeqTrainer:
    def __init__(self) -> None:
        pass

    def _train_epoch(self,
                     loader: DataLoader,
                     encoder: nn.Module,
                     decoder: nn.Module,
                     encoder_optimizer: optim.Adam,
                     decoder_optimizer: optim.Adam,
                     criterion: nn.NLLLoss) -> float:
        total_loss = 0.0
        for data in loader:
            x, y = data
            x = try_gpu(x)
            y = try_gpu(y)

            encoder_optimizer.zero_grad()
            decoder_optimizer.zero_grad()

            encoder_outputs, encoder_hidden = encoder(x)
            decoder_outputs, _, _ = decoder(encoder_outputs, encoder_hidden, y)

            loss = criterion(
                decoder_outputs.view(-1, decoder_outputs.size(-1)),
                y.view(-1)
            )
            loss.backward()

            encoder_optimizer.step()
            decoder_optimizer.step()

            total_loss += loss.item()
        
        return total_loss / len(loader)

    def train(self,
              loader: DataLoader,
              encoder: nn.Module,
              decoder: nn.Module,
              n_epochs: int,
              learning_rate: float=0.001,
              print_every: int=100) -> None:
        total_loss = 0.0
        encoder_optimizer = optim.Adam(encoder.parameters(), lr=learning_rate)
        decoder_optimizer = optim.Adam(decoder.parameters(), lr=learning_rate)
        criterion = nn.NLLLoss()

        encoder.train()
        decoder.train()
        for epoch in range(1, n_epochs+1):
            loss = self._train_epoch(loader, encoder, decoder, encoder_optimizer, decoder_optimizer, criterion)
            total_loss += loss

            if epoch % print_every == 0:
                average = total_loss / print_every
                total_loss = 0.0
                print(f"epoch {epoch}: {average}")
