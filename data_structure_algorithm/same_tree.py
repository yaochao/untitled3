#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/11/15


'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have hte same value.
'''


def isSameTree(p, q):
    if not p and not q:
        return True
    if p and q and p.val== q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False

def isSameTree2(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree2(p.left, q.left) and isSameTree2(p.right, q.right)
    return False

# Time Complexity O(min(N,M))
# Space Complexity O(min(height1, height2))