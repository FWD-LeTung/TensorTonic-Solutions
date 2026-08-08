import numpy as np
def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    # Write code here
    img = np.asarray(image)
    r = img.shape[0]
    c = img.shape[1]
    L = 256
    histogram = np.zeros(np.max(img)+1)
    for i in range(r):
        for j in range(c):
            histogram[img[i,j]] += 1
            
    prob = histogram / (r*c)
    
    cdf = np.cumsum(prob)
    
    x = np.min(cdf[cdf > 0])
    if x == 1:
       result = np.zeros_like(cdf)
    else:
       result = np.round(((cdf - x) / (1 - x)) * 255)

    return result[img].tolist()
    