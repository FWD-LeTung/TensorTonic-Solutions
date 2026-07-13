import torch
import torch.nn as nn

class Dropout(nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p
    def forward(self, x):
        """
        Returns: tensor with dropout applied
        """
        if self.p == 1.0:
            return torch.zeros_like(x)
        elif self.p == 0 or self.training==False:
            return x
        mask = (torch.rand(x.shape) >= self.p)
        return x*mask / (1-self.p)