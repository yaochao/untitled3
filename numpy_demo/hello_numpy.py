#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/15


import numpy as np


def ndarray_space():
    a = np.ndarray(shape=(2,2))
    b = np.array([[1,2],[1,3]])
    print(type(a))
    print(a)
    print(type(a))
    print(b)


if __name__ == '__main__':
    ndarray_space()
