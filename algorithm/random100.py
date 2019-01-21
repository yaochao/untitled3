#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2019/1/21

'''
从 [0,100] 随机取 10 个数，使之和等于 100，用 Python 如何实现，包含0和100
'''

import random


def main():
    nums = []
    for i in range(9):
        num = random.randint(0, 100)
        nums.append(num)
    nums.sort(reverse=True)
    nums.insert(0, 100)
    nums.insert(10, 0)
    print(nums)
    values = []
    for i in range(11):
        if i != 10:
            value = nums[i] - nums[i + 1]
            values.append(value)
    print(values)
    print(sum(values))


if __name__ == '__main__':
    main()
