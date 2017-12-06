#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/11/29


'''
二叉树的中序遍历
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    result = []
    if not root:
        return result
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result


def preorder(root):
    result = []
    if not root:
        return result
    stack = []
    while root or stack:
        while root:
            stack.append(root.left)
            stack.append(root.right)
            stack.append(root)



if __name__ == '__main__':
    n1 = Node(25)
    n2 = Node(50)
    n3 = Node(75)
    n4 = Node(100)
    n5 = Node(125)
    n6 = Node(150)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    print(inorder(n1))