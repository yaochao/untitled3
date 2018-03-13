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


def __main():
    jsfile = 'my_diff.js'
    r = exec_my_js(jsfile, 'getDiff', '你们好', '你好')
    print(r)


if __name__ == '__main__':
    __main()
