import cv2
import numpy as np
import matplotlib.pyplot as plt


def add_image(layout, index, image, title, gray=False):
    plt.subplot(*layout, index)
    plt.title(title)
    if gray:
        plt.imshow(image, cmap="gray")
    else:
        plt.imshow(image)


if __name__ == "__main__":
    image_path = r"../input/Lenna.jpg"
    src_image = cv2.imread(image_path)

    # convert BGR to RGB
    rgb_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
    add_image((2, 2), 1, rgb_image, "RGB-image")

    # split the image
    rgb_float_image = rgb_image.astype(np.float)
    r = rgb_float_image[:, :, 0]
    g = rgb_float_image[:, :, 1]
    b = rgb_float_image[:, :, 2]

    # Average component algorithm
    avg_float_image = (r + g + b) / 3
    avg_image = avg_float_image.astype(np.uint8)
    add_image((2, 2), 2, avg_image, "avg-gray", gray=True)

    # Psychological algorithm
    psy_float_image = 0.299 * r + 0.587 * g + 0.144 * b
    psy_image = psy_float_image.astype(np.uint8)
    add_image((2, 2), 3, psy_image, "psy-gray", gray=True)

    # opencv
    cv2_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
    add_image((2, 2), 4, cv2_image, "cv2-gray", gray=True)

    plt.show()
