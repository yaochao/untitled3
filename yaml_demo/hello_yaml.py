#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/21


import yaml

with open('hello.yml', 'r') as f:
    y = yaml.load(f.read())
    print(type(y))
    for i in y:
        print(i)