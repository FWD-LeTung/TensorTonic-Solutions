import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    x = np.array(data, dtype=np.float64)
    y1 = np.where(x>threshold, 1., 0.)
    cond1 = np.any(x>threshold, axis=1)
    cond2 = np.all(x>threshold, axis=1)
    y2 = np.empty_like(x)
    y3 = np.empty_like(x)
    for i, value in enumerate(cond1):
        if value:
            y2[i] = x[i].copy()
        else:
            y2[i] = np.zeros(x[i].shape)
    
    for i, value in enumerate(cond2):
        if value:
            y3[i] = x[i].copy()
        else:
            y3[i] = np.zeros(x[i].shape)
    return np.stack([y1, y2, y3], axis=0)