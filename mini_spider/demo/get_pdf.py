#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/15


import requests
import time

def get_file(url, index):
    r = requests.get(url)
    if r.status_code == 200:
        with open('pdf2/{}.jpg'.format(index), 'wb') as f:
            f.write(r.content)

def get_all_file():
    for i in range(80, 224):
        url = 'http://apabi.lib.pku.edu.cn/OnLineReader/command/imagepage.ashx?objID=m.20081230-m801-w015-032.ft.cebx.2&metaId=m.20081230-m801-w015-031&OrgId=pku&Ip=undefined&scale=1.019063998345077&width=784&height=1157&pageid={}&ServiceType=Imagepage&scaleType=1&OrWidth=769.333428786796&OrHeight=1136.00014291197&testres=&debug=&SessionId=B1E796EBDA2705E3&UserName=%E6%9D%A5%E8%87%AA%20222.29.114.54%20%E7%9A%84%E7%94%A8%E6%88%B7&cult=CN&rights=1-0_00&time=2017-12-21%2012:28:14&sign=60B71535051D4ADE7BB84D87C29F757D'.format(i)
        get_file(url, i)
        print(i)

# def gen_pdf():
#     for i in range(213):
#         file_path = 'pdf2/{}.jpg'.format(i+1)
#         pass


if __name__ == '__main__':
    get_all_file()