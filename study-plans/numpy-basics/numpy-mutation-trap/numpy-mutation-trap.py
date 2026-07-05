import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    x = np.array(data, dtype=np.float64)
    return np.stack((x[row_idx],np.clip(x[row_idx], lo, hi)))