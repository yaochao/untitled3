#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2019/3/13


"""
读取十万张图片，打印出图片的size
"""
from PIL import Image


def read_images():
    fp = 'mm.jpg'
    image = Image.open(fp)
    print(image.size)


def main():
    for i in range(100000):
        read_images()


if __name__ == '__main__':
    main()
