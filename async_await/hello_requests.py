#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/9/13
import time

import requests

def request():
    url = 'https://survey.news.ifeng.com/api/accumulator?format=js&key=http%3A%2F%2Ftech.ifeng.com%2Fa%2F20180913%2F45164247_0.shtml%3Fcry'
    response = requests.get(url)
    print(response.text)

start = time.time()
for _ in range(1000):
    request()

print('cost: ', time.time() - start)
