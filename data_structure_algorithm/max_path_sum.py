#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/11/14

maximum = float('-inf')

def max_sum():
    pass

def helper(root):
    if not root:
        return 0
    left = helper(root.left)
    right = helper(root.right)
    maximum = max(maximum, left + right + root.val)
    return maximum + max(left, right)