import numpy as np
import matplotlib.pyplot as plt
import cv2


def add_show_image(img, index, title):
    plt.subplot(1, 2, index)
    plt.imshow(img)
    plt.title(title)


if __name__ == "__main__":
    image_path = r"../input/Lenna.jpg"
    src_image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
    add_show_image(rgb_image, 1, "src-image")

    pts1 = np.array([[0, 0], [1, 0], [0, 1]], dtype=np.float32)
    pts2 = np.array([[100, 50], [101, 50], [100, 51]], dtype=np.float32)
    matrix = cv2.getAffineTransform(pts1, pts2)

    affine_image = cv2.warpAffine(rgb_image, matrix, rgb_image.shape[:2])
    add_show_image(affine_image, 2, "aff-image")

    plt.show()

