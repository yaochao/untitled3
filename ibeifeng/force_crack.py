#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/9/29

import threading

import requests


class MyThread(threading.Thread):
    def __init__(self, target=None, args=()):
        super(MyThread, self).__init__()
        self.target = target
        self.args = args

    def run(self):
        self.result = self.target(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def get_status_code(url):
    s = requests.session()
    s.keep_alive = False
    status_code = s.head(url=url).status_code
    print(status_code)
    if status_code == 200:
        print(url)
    return status_code


def main():
    threads = []
    for i in range(0, 65536):
        i = str(hex(i)[2:])
        url = 'http://fvideo.ibeifeng.com/' + 'e8602d72-5ae4-11e7-' + i + '-b82a72dbe2ed.mp4'
        t = MyThread(target=get_status_code, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        status_code = t.get_result()
        if status_code == 200:
            break


if __name__ == '__main__':
    main()
