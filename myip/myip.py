#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2022/1/24

import requests


def get_myip():
    response = requests.get("https://myip.ipip.net")
    t = response.text
    print(t)


if __name__ == '__main__':
    get_myip()
