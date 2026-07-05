import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    x = np.array(data, dtype=np.float64)
    y = x[row_start:row_stop,:]
    mask = y > threshold
    return y[mask]