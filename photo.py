import pixel
import numpy as np
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

def save_photo(matrix, filename):
    plt.figure(figsize=(6, 6))
    plt.imshow(matrix, cmap='gray')
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()

def new_photo(matrix):
    new = np.zeros((16, 16))
    for x, y in np.nditer((matrix, new), op_flags=[['readonly'],['readwrite']]):
        if x == 1:
            result = pixel.test_pixel(True)
            if result == "FUNCTIONAL":
                y[...] = 1

    return new

if __name__ == "__main__":
    photo = create_photo()
    new = new_photo(photo)
    save_photo(photo, "gato.png")
    save_photo(new, "gato_cuantico.png")
