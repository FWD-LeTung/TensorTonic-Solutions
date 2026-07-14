import torch

def softmax(logits):
    """
    Returns: tensor of same shape with softmax probabilities (each row sums to 1)
    """
    x = torch.tensor(logits)
    max = torch.max(x, dim=1, keepdim=True).values
    exp = torch.exp(x - max)
    return exp / torch.sum(exp, dim=1, keepdim=True)
