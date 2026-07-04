import numpy as np

def create_sequence(start, stop, param, kind):
    """
    Returns: 1D ndarray of float64 values
    """
    if kind == 'linspace':
        return np.linspace(start, stop, param, dtype = np.float64)
    return np.arange(start, stop, param, dtype = np.float64)
