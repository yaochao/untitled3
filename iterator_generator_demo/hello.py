#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/28

import time


def get_image_by_id(n):
    time.sleep(1)
    return n


def get_images(n):
    result = []
    for i in range(n):
        result.append(get_image_by_id(i))
    return result


images = get_images(100)

# 改造一下希望能够进行懒执行(有空的时候再去执行，不是每次都必须全部处理完成)，因为get_image_by_id是一个耗时的操作
image_id = -1


def next_image():
    global image_id
    image_id += 1
    return get_image_by_id(image_id)


image0 = next_image()
image1 = next_image()


# 使用全局变量决定了 next_image 无法被两个个体使用。例如两个人都想从头获取图片，这是没法完成的，因此我们定义一个类来解决这个问题
class ImageRepository:
    def __init__(self):
        self.image_id = -1

    def next_image(self):
        self.image_id += 1
        return get_image_by_id(self.image_id)


repo1 = ImageRepository()
image2 = repo1.next_image()
image3 = repo1.next_image()

repo2 = ImageRepository()
image4 = repo2.next_image()
image5 = repo2.next_image()


# 如果你熟悉 iterator 的话，应该知道上面这个需求是一个典型的 iterator，因此我们可以实现 __iter__ 及 __next__ 方法来将它变成一个 iterator，从而充分利用 iterator 现成的一些工具：
class ImageRepositoryIteror:
    def __init__(self):
        self.image_id = -1

    def __next__(self):
        return self

    def __iter__(self):
        self.image_id += 1
        return get_image_by_id(self.image_id)


for i in ImageRepositoryIteror():
    print(i)


# 从 iterator 到 generator
# 在 Python 中，只要一个函数中使用了 yeild 这个关键字，就代表这个函数是一个生成器 (generator)。而 yield 的作用就相当于让 Python 帮我们把一个“串行”的逻辑转换成 iterator 的形式
def image_repository_generator():
    image_id = -1
    while True:
        image_id += 1
        yield get_image_by_id(image_id)


for i in image_repository_generator():
    print(i)


# 斐波那契数列，使用 generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# 斐波那契数列，使用 iterator
class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
