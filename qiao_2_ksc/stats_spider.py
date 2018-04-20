#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/20


from requests_html import HTMLSession
from urllib.parse import urljoin


def send_request():
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/15/22/152222.html'
    session = HTMLSession()
    r = session.get(url)
    village_code_map = {}
    village_code_list = []
    for i in r.html.xpath('//*[@class="towntr"]/td[2]/a/@href'):
        url2 = urljoin(url, i)
        r2 = session.get(url2)
        codes = r2.html.xpath('//*[@class="villagetr"]/td[1]/text()')
        names = r2.html.xpath('//*[@class="villagetr"]/td[3]/text()')
        for i in range(len(codes)):
            village_code_map[codes[i]] = names[i]
            village_code_list.append(codes[i])
    return village_code_map


def go():
    village_code_map = send_request()
    print(village_code_map.keys()[village_code_map.values().index('二队')])


if __name__ == '__main__':
    go()
