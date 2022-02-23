import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    matrix = np.array([
        [000, 255, 000],
        [100, 150, 200],
        [255, 240, 000]
    ])
    plt.imshow(matrix, cmap="gray")
    plt.show()
