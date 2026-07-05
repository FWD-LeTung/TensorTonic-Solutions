import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    x = np.array(data, dtype=np.float64)
    y1 = (x>threshold).astype(np.float64)
    cond1 = np.any(x>threshold, axis=1)
    cond2 = np.all(x>threshold, axis=1)
    y2 = np.empty_like(x)
    y3 = np.empty_like(x)
    y2 = np.where(cond1[:,np.newaxis], x, 0.0)
    y3 = np.where(cond2[:,np.newaxis], x, 0.0)
    return np.stack([y1, y2, y3], axis=0)