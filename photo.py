import pixel
import numpy as np
from PIL import Image 

def load_bw_photo(file, height, width, threshold, invert):
    img = Image.open(file).convert("L")
    size = (width, height)
    img = img.resize(size, Image.LANCZOS)
    photo = np.array(img)
    matrix = (photo > threshold).astype(np.float64)

    if invert:
        matrix = 1 - matrix

    return matrix

def new_photo(matrix):
    new = np.zeros(matrix.shape)
    for x, y in np.nditer((matrix, new), op_flags=[['readonly'],['readwrite']]):
        result = pixel.test_pixel(x == 1)
        if result == "FUNCTIONAL":
            y[...] = 1

    return new


