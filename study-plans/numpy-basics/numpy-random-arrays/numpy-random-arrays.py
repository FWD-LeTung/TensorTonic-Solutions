import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    np.random.seed(seed)
    if kind == 'uniform':
        return np.random.uniform(size=tuple(shape)).astype(np.float64)
    else:
        return np.random.normal(size=tuple(shape)).astype(np.float64)
        
