import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    data = np.asarray(X, dtype=float)
    mean = np.mean(data,axis=axis, keepdims=True)
    std = np.std(data,axis=axis, keepdims=True) + eps
    z = (data - mean) / std
    return z