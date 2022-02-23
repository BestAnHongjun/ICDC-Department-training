import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    matrix = np.array([
        [[255, 000, 000], [000, 255, 000], [000, 000, 255]],
        [[255, 255, 000], [255, 000, 255], [000, 255, 255]],
        [[000, 000, 000], [255, 255, 255], [100, 100, 200]]
    ])
    plt.imshow(matrix)
    plt.show()
