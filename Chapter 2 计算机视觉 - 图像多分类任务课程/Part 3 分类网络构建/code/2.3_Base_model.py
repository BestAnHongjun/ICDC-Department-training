# -*- coding:utf-8 -*-
# nn.Module.py
# 2022/1/12 15:34 p.m.
import torch
from torch import nn
import torch.nn.functional as F


# ====================最基本的网络结构====================
# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()  # 超继承父类，必备
#
#     def forward(self, input):
#         output = input + 1
#         return output
#
#
# model = Model()
# x = torch.tensor(1.0)
# output = model(x)
# print(output)  # tensor(2.)

# ====================卷积====================
# input = torch.tensor([[1, 2, 0, 3, 1],
#                       [0, 1, 2, 3, 1],
#                       [1, 2, 1, 0, 0],
#                       [5, 2, 3, 1, 1],
#                       [2, 1, 0, 1, 1]])
#
# kernel = torch.tensor([[1, 2, 1],
#                        [0, 1, 0],
#                        [2, 1, 0]])
#
# # torch 尺寸变换
# input = torch.reshape(input, (1, 1, 5, 5))  # 1个batch_size，1个通道，5x5
# kernel = torch.reshape(kernel, (1, 1, 3, 3))
#
# """
# 为什么要做尺寸变换:
# 在Conv2d函数说明中，它需要传入的是一个四维的tensor数据，而目前我们的tensor只有2维，显然不能满足需求。
# 第一个参数代表batch_size，第二个参数代表通道数channel，三、四参数代表了图像矩阵的宽和高。
# """
#
# output = F.conv2d(input, kernel, stride=1)
# print(output)
