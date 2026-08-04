import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    img = np.asarray(image)
    result = np.zeros(256)
    shape = img.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            result[img[i][j]] +=1
    return result.tolist()