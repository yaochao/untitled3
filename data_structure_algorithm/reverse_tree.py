#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/11/17


'''
翻转二叉树
'''


def reverse(node):
    if not node:
        return
    node.left, node.right = node.right, node.left
    if node.left:
        reverse(node=node.left)
    if node.right:
        reverse(node=node.right)
