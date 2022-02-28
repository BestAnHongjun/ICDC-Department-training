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

    src_shape = rgb_image.shape
    cx, cy = src_shape[0] / 2, src_shape[1] / 2
    matrix = cv2.getRotationMatrix2D((cx, cy), 30, 1.0)

    affine_image = cv2.warpAffine(rgb_image, matrix, rgb_image.shape[:2])
    add_show_image(affine_image, 2, "aff-image")

    plt.show()

