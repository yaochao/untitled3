#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/10

'''
方案一：（参考网上代码，感觉实用性不是很强）使用PIL截取图像，然后将RGB转为HSV进行判断，统计判断颜色，最后输出RGB值
http://www.sharejs.com/codes/python/8655
'''

import colorsys
from PIL import Image
import requests
import os


def get_image():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    url = 'http://www.dianhua.cn/appeal/code/'
    response = requests.get(url)
    if response.status_code == 200:
        filename = 'code.png'
        with open(filename, 'wb') as f:
            f.write(response.content)
            return os.path.join(base_dir, filename)


def get_dominant_color(image):
    max_score = 0.0001
    dominant_color = None
    for count, (r, g, b) in image.getcolors(image.size[0] * image.size[1]):
        # 转为HSV标准
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)

        # 忽略高亮色
        if y > 0.9:
            continue
        score = (saturation + 0.1) * count
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    return dominant_color


def rgb_filter(img, rgb):
    '''
    过滤掉不等于给定的rgb的rgb值，设置为255,255,255
    :param img: Image对象，需要转换为RGB模式
    :param rgb: 给定RGB
    :return: 过滤之后的
    '''
    size = img.size
    img = img.convert('RGB')
    for i in range(size[0]):
        for j in range(size[1]):
            tmp_rgb = img.getpixel((i, j))
            if rgb != tmp_rgb:
                img.putpixel((i, j), (255, 255, 255))
            else:
                coordinates = [(i - 1, j), (i - 1, j - 1), (i, j - 1)]
                for x, y in coordinates:
                    # 把超出边界的像素加工一下
                    if x < 0:
                        x = 0
                    elif x >= size[0]:
                        x = size[0] - 1
                    if y < 0:
                        y = 0
                    elif y >= size[1]:
                        y = size[1] - 1
                    img.putpixel((x, y), rgb)
    return img


def rgb2img(rgb, size):
    '''
    RGB对应的颜色画出来
    :param rgb:
    :return:
    '''
    img = Image.new("RGB", size, rgb)
    return img


def paste_imgs(*imgs):
    length = 0
    width = 0
    for img in imgs:
        w, l = img.size
        length = w if w > length else length
        width += l

    new_img = Image.new('RGBA', (length, width))
    tmp_width = 0
    for i in range(len(imgs)):
        img = imgs[i]
        w, l = img.size
        new_img.paste(img, (0, tmp_width))
        tmp_width += l
    return new_img


def main():
    imgname = get_image()
    # imgname = 'code.png'
    if not imgname:
        return
    img1 = Image.open(imgname)
    image = img1.convert('RGB')
    rgb = get_dominant_color(image)

    # 过了掉不是主色的rgb值
    img2 = rgb_filter(img1, rgb)

    img3 = rgb2img(rgb, img1.size)
    img4 = paste_imgs(image, img2, img3)
    img4.show()

    print('main color:', rgb)


if __name__ == '__main__':
    main()
