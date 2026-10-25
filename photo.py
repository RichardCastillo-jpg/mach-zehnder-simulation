import pixel
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt

def create_photo():
    photo = [
    "................",
    "...#........#...",
    "...##......##...",
    "...###....###...",
    "...##########...",
    "..###.####.###..",
    ".####.####.####.",
    ".####.####.####.",
    ".##############.",
    ".#####....#####.",
    "..#####..#####..",
    "...##########...",
    "....########....",
    ".....######.....",
    "................",
    "................",
    ]


    photo_np = np.array([list(row) for row in photo])
    matrix = (photo_np == "#").astype(np.int32)
    return matrix

def load_bw_photo(path, size, threshold=100):
    img = Image.open(path).convert("L")
    img = img.resize(size, Image.LANCZOS)
    photo = np.array(img)
    matrix = (photo > threshold).astype(np.int32)
    return matrix
    

def save_photo(matrix, filename):
    plt.figure(figsize=(6, 6))
    plt.imshow(matrix, cmap='gray')
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()

def new_photo(matrix):
    new = np.zeros(matrix.shape)
    for x, y in np.nditer((matrix, new), op_flags=[['readonly'],['readwrite']]):
        result = pixel.test_pixel(x == 1)
        if result == "FUNCTIONAL":
            y[...] = 1

    return new


