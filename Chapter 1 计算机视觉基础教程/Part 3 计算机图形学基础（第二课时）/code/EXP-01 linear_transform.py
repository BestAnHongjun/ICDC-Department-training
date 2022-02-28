import numpy as np
import matplotlib.pyplot as plt
import cv2


def interpolation(src, dst_coord):
    x = dst_coord[0][0]
    y = dst_coord[1][0]
    if x < 0 or x >= src.shape[0]:
        return np.zeros(src.shape[2])
    if y < 0 or y >= src.shape[1]:
        return np.zeros(src.shape[2])
    x1, x2 = int(x), int(x) + 1
    y1, y2 = int(y), int(y) + 1
    if x2 >= src.shape[0]:
        x2 = x1 - 1
    if y2 >= src.shape[1]:
        y2 = y1 - 1
    f_r1 = ((x2-x) * src[x1, y1, :] + (x-x1) * src[x2, y1, :]) / (x2 - x1)
    f_r2 = ((x2-x) * src[x1, y2, :] + (x-x1) * src[x2, y2, :]) / (x2 - x1)
    f = ((y2-y) * f_r1 + (y-y1) * f_r2) / (y2-y1)
    return f


def apply_transform(src, trans_matrix, dst_shape):
    dst = np.zeros((*dst_shape, src.shape[2]))
    for h in range(dst_shape[0]):
        for w in range(dst_shape[1]):
            src_coord = np.array([[h], [w]])
            dst_coord = np.dot(trans_matrix, src_coord)
            dst[h, w, :] = interpolation(src, dst_coord)
    return dst


def zoom(src, dst_shape):
    fx = dst_shape[0] / src.shape[0]
    fy = dst_shape[1] / src.shape[1]
    zoom_matrix = np.array([
        [fx, 0],
        [0, fy]
    ])
    zoom_matrix = np.linalg.inv(zoom_matrix)
    dst = apply_transform(src, zoom_matrix, dst_shape)
    return dst


def shear(src, rate):
    shear_matrix = np.array([
        [1, rate],
        [0, 1]
    ])
    shear_matrix = np.linalg.inv(shear_matrix)
    dst = apply_transform(src, shear_matrix, src.shape[:2])
    return dst


def rotate(src, rad):
    rotate_matrix = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad), np.cos(rad)]
    ])
    rotate_matrix = np.linalg.inv(rotate_matrix)
    dst = apply_transform(src, rotate_matrix, src.shape[:2])
    return dst


def add_show_image(img, index, title):
    plt.subplot(2, 2, index)
    plt.imshow(img)
    plt.title(title)


if __name__ == "__main__":
    image_path = r"../input/Lenna.jpg"
    src_image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
    rgb_float_image = rgb_image.astype(np.float)
    add_show_image(rgb_image, 1, "src-image")

    zoom_float_image = zoom(rgb_float_image, (200, 300))
    zoom_image = zoom_float_image.astype(np.uint8)
    add_show_image(zoom_image, 2, "zoom-image")

    shear_float_image = shear(rgb_float_image, 0.3)
    shear_image = shear_float_image.astype(np.uint8)
    add_show_image(shear_image, 3, "shear-image")

    rotate_float_image = rotate(rgb_float_image, np.pi / 6)
    rotate_image = rotate_float_image.astype(np.uint8)
    add_show_image(rotate_image, 4, "rotate-image")

    plt.show()
