import torchvision
from torch.utils.data import DataLoader


dataset_transform = torchvision.transforms.Compose([
                                  torchvision.transforms.ToTensor()
                            ])

# root: 当前数据集下载路径
# train:是否作为训练集出现，True为训练集，False为测试集
# download:是否下载数据集

train_set = torchvision.datasets.CIFAR10(root='./dataset',
                                         train=True,
                                         transform=dataset_transform,
                                         download=True)

test_set = torchvision.datasets.CIFAR10(root='./dataset',
                                         train=False,
                                         transform=dataset_transform,
                                         download=True)

# datasets:要加载的数据集
# batch_size:相当于我们在datasets这个牌堆里每次“抽几张牌”（一次加载多少张图片）
# shuffle:是否将数据集打乱顺序，最好设为True

# 准备一个测试数据集
test_data = torchvision.datasets.CIFAR10("./dataset", train=False, transform=torchvision.transforms.ToTensor())

test_loader = DataLoader(test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=False)


# 测试数据集中第一张样本的大小及target (label)
# img, target = test_data[0]
# print(img.shape)
# print(target)

# 将测试集图片全部输出
# for data in test_loader:
#     imgs, targets = data
#     print(imgs.shape)
#     print(targets)
