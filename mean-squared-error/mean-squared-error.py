import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    pred =  np.asarray(y_pred, dtype=np.float32)
    label =  np.asarray(y_true, dtype=np.float32)
    loss = sum((pred-label)**2) / len(pred)

    return loss