from PIL import Image
from torchvision import transforms
import cv2

img = Image.open("./text.jpg")  # 打开指定位置的图片



# ToTensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
# print(img_tensor)


# Normalize
# print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
img_norm = trans_norm(img_tensor)


# Resize
print(img.size)  # 读取大小
trans_resize = transforms.Resize((800, 700))  # 700 x 800
# trans_resize_2 = transforms.Resize(648) # 方法2，等比缩放
img_resize = trans_resize(img)
# img_resize = trans_totensor(img_resize)
print(img_resize.size)
