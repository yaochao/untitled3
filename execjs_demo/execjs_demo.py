#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/2/28

import execjs


def get_js(jsfile):
    with open(jsfile, encoding='utf-8') as f:
        js = f.read()
        return js


def exec_my_js(jsfile, func_str, *params):
    js = get_js(jsfile)
    ctx = execjs.compile(js)
    r = ctx.call(func_str, *params)
    return r

def get_diff(text1, text2):
    jsfile = '/Users/yaochao/python/PycharmProjects/untitled3/execjs_demo/my_diff.js'
    diff = exec_my_js(jsfile, 'getDiff', text1, text2)
    return diff


def __main():
    diff = get_diff('你们好', '你好')
    print(diff)


if __name__ == '__main__':
    __main()
