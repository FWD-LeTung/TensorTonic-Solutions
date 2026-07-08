import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    x = np.array(data, dtype=np.float64)
    y = np.sort(x, axis=axis)
    z = np.argsort(x, axis=axis).astype(np.float64)
    return np.stack([y,z])