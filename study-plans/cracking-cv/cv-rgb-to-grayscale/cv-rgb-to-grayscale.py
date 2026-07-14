import numpy as np
def rgb_to_grayscale(image):
    """
    Returns: 2D list of shape (H, W) with luma values rounded to 4 decimals
    """
    x = np.array(image)
    r = x[:, :, 0]
    g = x[:, :, 1]
    b = x[:, :, 2]
    y = r*0.299 + 0.587*g + 0.114*b
    return y.tolist()
