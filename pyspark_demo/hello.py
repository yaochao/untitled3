#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/14


import json
import sys


def transfer(j):
    d = json.loads(j)
    s = ''
    for k, v in d.items():
        v = r'\N' if not v else v
        s += k + '~' + v + '|'
    return s[:-1]


def main(args):
    try:
        j = args[1]
        print(type(j))
        assert type(j) == str
        print(transfer(j))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(sys.argv)
