import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    x = np.array(data, dtype=np.float64)
    weights = np.array(weights, np.float64)
    return x*weights