#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/16


import requests
from lxml import etree


def get_xici():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    response = requests.get(url='http://www.xicidaili.com/nn/', headers=headers)
    if response.status_code == 200:
        selector = etree.HTML(response.text)
        trs = selector.xpath('//tr')
        http_proxies = []
        https_proxies = []
        for tr in trs[1:]:
            ip = tr.xpath('td[2]/text()')[0]
            port = tr.xpath('td[3]/text()')[0]
            schema = tr.xpath('td[6]/text()')[0]
            schema = str.lower(schema)
            result = test_ip(schema=schema, ip=ip, port=port)
            if result:
                if schema == 'http':
                    http_proxies.append({schema: schema + '://' + ip + ':' + port })
                else:
                    https_proxies.append({schema: schema + '://' + ip + ':' + port })
        return http_proxies, https_proxies


def test_ip(schema, ip, port):
    proxies = {
        schema: schema + '://' + ip + ':' + port
    }
    if schema == 'http':
        url = 'http://httpbin.org/ip'
    else:
        url = 'https://httpbin.org/ip'
    try:
        response = requests.get(url=url, proxies=proxies, timeout=1)
        if response.status_code == 200:
            if response.json()['origin'] == ip:
                return [schema, ip, port]
    except Exception as e:
        # print(e)
        return None


if __name__ == '__main__':
    get_xici()
