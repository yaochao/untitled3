#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2022/1/24

import urllib.request
import socket


def get_public_ip():
    with urllib.request.urlopen("https://ip.tool.lu") as response:
        html = response.read().decode('utf8')
        print(html)


def get_local_ip():
    print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
           [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])


if __name__ == '__main__':
    get_local_ip()
    get_public_ip()
