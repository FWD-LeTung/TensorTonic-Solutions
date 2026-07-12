import torch

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    Returns: tensor of shape (N, D), the batch-normalized output
    """
    x = torch.tensor(X, dtype=torch.float32)
    mean = x.mean(dim=0)
    var = x.var(dim=0, unbiased=False)
    x_norm = (x-mean) / torch.sqrt(var + eps)
    return gamma*x_norm + beta
