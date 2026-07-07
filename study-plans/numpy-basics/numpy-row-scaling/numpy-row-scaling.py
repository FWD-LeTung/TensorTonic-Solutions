import numpy as np

def scale_rows(data, weights):
    """Returns: np.ndarray of shape (m, n), each row scaled by corresponding weight"""
    a = np.asarray(data, dtype=np.float64)
    s = np.asarray(weights, dtype=np.float64)

    
    return a * s[:, np.newaxis]