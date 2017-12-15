#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/15


import requests
import time

def get_file(url, index):
    r = requests.get(url)
    if r.status_code == 200:
        with open('pdf/{}.jpg'.format(index), 'wb') as f:
            f.write(r.content)

def get_all_file():
    for i in range(353):
        url = 'http://apabi.lib.pku.edu.cn/OnLineReader/command/imagepage.ashx?objID=7-81034-934-1.ft.cebx.1&metaId=7-81034-934-1&OrgId=pku&Ip=undefined&scale=1.186781591510979&width=826&height=1151&pageid={}&ServiceType=Imagepage&scaleType=1&OrWidth=696.000010371208&OrHeight=970.666597141225&testres=&debug=&SessionId=58B3B4CCAADD6FBC&UserName=%E6%9D%A5%E8%87%AA%20222.29.112.66%20%E7%9A%84%E7%94%A8%E6%88%B7&cult=CN&rights=1-0_00&time=2017-12-15%2010:32:47&sign=79B7BE91791D6A502522972F50703CB4'.format(i)
        get_file(url, i)
        time.sleep(2)
        print(i)

def gen_pdf():
    for i in range(352):
        file_path = 'pdf/{}.jpg'.format(i+1)


if __name__ == '__main__':
    get_all_file()