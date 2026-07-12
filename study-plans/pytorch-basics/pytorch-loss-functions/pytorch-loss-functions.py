import torch

def compute_loss(pred, target, method, delta=1.0):
    """
    Returns: float, the mean loss value
    """
    y1 = torch.tensor(pred, dtype=torch.float32)
    y2 = torch.tensor(target, dtype=torch.float32)
    n = len(y1)
    if method == "mse":
        return (torch.sum((y2-y1)**2) / n).item() 
    elif method == "cross_entropy":
        y2 = torch.tensor(target, dtype=torch.long)
        logsumexp = torch.logsumexp(y1, dim=1)
        correct_logits = y1[torch.arange(y1.size(0)), y2]
        loss = logsumexp - correct_logits
        return loss.mean().item()
    else:
        diff = (y2 - y1).abs()
        loss = torch.where(diff > delta, delta*(diff - delta*0.5), (diff**2)*0.5)
        return loss.mean().item()
        
