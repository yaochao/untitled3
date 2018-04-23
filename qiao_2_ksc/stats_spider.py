#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/20


from requests_html import HTMLSession
from urllib.parse import urljoin


def get_village_code_map():
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/15/22/152222.html'
    session = HTMLSession()
    r = session.get(url)
    village_code_map = {}
    for i in r.html.xpath('//*[@class="towntr"]/td[2]/a/@href'):
        url2 = urljoin(url, i)
        r2 = session.get(url2)
        codes = r2.html.xpath('//*[@class="villagetr"]/td[1]/text()')
        names = r2.html.xpath('//*[@class="villagetr"]/td[3]/text()')
        assert len(codes) == len(names)
        for i in range(len(codes)):
            name = names[i]
            code = codes[i]
            village_code_map[code] = name
    return village_code_map


def get_village_code_map2():
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/15/22/152222.html'
    session = HTMLSession()
    r = session.get(url)
    village_code_map = {}
    village_code_map2 = {}
    for i in r.html.xpath('//*[@class="towntr"]/td[2]/a/@href'):
        url2 = urljoin(url, i)
        r2 = session.get(url2)
        town_code = url2.split('/')[-1].split('.')[0]
        codes = r2.html.xpath('//*[@class="villagetr"]/td[1]/text()')
        names = r2.html.xpath('//*[@class="villagetr"]/td[3]/text()')
        assert len(codes) == len(names)
        for i in range(len(codes)):
            name = names[i]
            code = codes[i]
            village_code_map[code] = name
            village_code_map2[name] = code

    for i in village_code_map.keys():
        if i not in village_code_map2.values():
            print(village_code_map[i])

    print(len(village_code_map.keys()), len(village_code_map2.keys()))
    return village_code_map


if __name__ == '__main__':
    print(len(get_village_code_map().keys()))
    print(get_village_code_map())
