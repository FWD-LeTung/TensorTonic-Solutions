import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype=torch.float32)
    if method == "relu":
        y = torch.zeros(len(x))
        return torch.maximum(x,y).tolist()
    elif method == "leaky_relu":
        return torch.where(x>0, x, 0.01*x).tolist()
    elif method == "sigmoid":
        result = 1 / (1+ torch.exp(-x))
        return result.tolist()
    else:
        result = (torch.exp(x)-torch.exp(-x)) / (torch.exp(x)+torch.exp(-x))
        return result.tolist()        