# -*- coding:utf-8 -*-
# nn.Module.py
# 2022/1/12 15:34 p.m.

# ====================Conv2d()====================
import torch
import torchvision
from torch.utils.data import DataLoader
from torch import nn
# from torch.nn import Conv2d
#
#
# # 下载数据集
# dataset = torchvision.datasets.CIFAR10("./dataset", train=True, transform=torchvision.transforms.ToTensor(), download=True)
#
# dataloader = DataLoader(dataset, batch_size=64)
#
#
# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=(3, 3), stride=1, padding=0)
#
#     def forward(self, x):
#         self.conv1(x)
#         return x
#
#
# model = Model()
# print(model)
#
# for data in dataloader:
#     imgs, targets = data
#     output = model(imgs)
#     print(imgs.shape)
#     print(output.shape)

# ====================MaxPool2d()====================

# input = torch.tensor([[1, 2, 0, 3, 1],
#                       [0, 1, 2, 3, 1],
#                       [1, 2, 1, 0, 0],
#                       [5, 2, 3, 1, 1],
#                       [2, 1, 0, 1, 1]], dtype=torch.float32)
# # 如果不改成浮点数会报错
#
# # 若第一个参数设为-1，则它过后会自动计算实际的值
# input = torch.reshape(input, (-1, 1, 5, 5))
# print(input.shape)
#
#
# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         self.maxpool1 = nn.MaxPool2d(kernel_size=3, ceil_mode=True)
#
#     def forward(self, input):
#         output = self.maxpool1(input)
#         return output
#
#
# model = Model()
# output = model(input)
# print(output)

# ====================ReLU()====================
# import torch
#
# input = torch.tensor([[1, -0.5],
#                       [-1, 3]])
#
# input = torch.reshape(input, (-1, 1, 2, 2))
# print(input.shape)
#
#
# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         self.relu1 = nn.ReLU()
#
#     def forward(self, input):
#         output = self.relu1(input)
#         return output
#
#
# model = Model()
# output = model(input)
# print(output)


# ====================Vgg16Net()====================
# import torch.nn as nn
# import torch
#
# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         self.model1 = nn.Sequential(
#             nn.Conv2d(3, 32, kernel_size=5, padding=2),
#             nn.MaxPool2d(2),
#             nn.Conv2d(32, 32, 5, padding=2),
#             nn.MaxPool2d(2),
#             nn.Conv2d(32, 64, 5, padding=2),
#             nn.MaxPool2d(2),
#             nn.Flatten(),
#             nn.Linear(1024, 64),
#             nn.Linear(64, 10)
#         )
#
#     def forward(self, x):
#         x = self.model1(x)
#         return x
#
#
# model = Model()
# print(model)
#
# # 可以理解成是这个tensor里有64张图片，每张都是彩色（3通道的）、宽32高32。
# input = torch.ones(64, 3, 32, 32)
# output = model(input)
# print(output.shape)
