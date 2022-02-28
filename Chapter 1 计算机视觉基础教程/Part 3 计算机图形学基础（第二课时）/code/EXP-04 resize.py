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

    resize_image = cv2.resize(rgb_image, (100, 200))
    add_show_image(resize_image, 2, "resize-image")

    plt.show()

