#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/23


import ctypes

hello_lib = ctypes.cdll.LoadLibrary('hello.so')

hello = hello_lib.hello
hello('Hello World')
# TODO：将Python字符串传递给C，是有问题的。上面那个只能打印出一个H（python2没事，python3有问题）