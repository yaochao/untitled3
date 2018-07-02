#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/6/30


'''
行政区划码2016爬虫
'''
import copy
import time
import user_agent

import pymysql
from urllib.parse import urljoin

from requests_html import HTMLSession

MYSQL_CONF_DEV = {
    'host': '10.69.57.77',
    'port': 8891,
    'user': 'phstest',
    'passwd': 'phstest@20161205',
    'db': 'g_lb',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
MYSQL_CONF_LOCAL = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'toor',
    'db': 'work',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
connection = pymysql.Connect(**MYSQL_CONF_LOCAL)
connection2 = pymysql.Connect(**MYSQL_CONF_DEV)
session = HTMLSession()
proxies = {
  "http": "http://127.0.0.1:1087",
  "https": "http://127.0.0.1:1087",
}

def save_to_mysql(params):
    try:
        cursor = connection.cursor()
        sql = 'insert into zd_area2 (bm,mc,sjbm) values (%s,%s,%s)'
        print(params)
        cursor.execute(sql, params)
        connection.commit()
    except Exception as e:
        print(e)

def get_provinces():
    start_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html'
    r = session.get(start_url, headers={'user-agent': user_agent.generate_user_agent()})
    provinces = r.html.find('.provincetr td a')
    print(len(provinces))
    # 一共31个
    for i in provinces:
        text = (i.text)
        url = i.absolute_links
        url2 = copy.deepcopy(url)
        code = url.pop().split('/')[-1].split('.html')[0]
        print(text)
        save_to_mysql((code, text, '0'))
        get_city(url2.pop(), code)


def get_city(url, parent_code):
    r = session.get(url, headers={'user-agent': user_agent.generate_user_agent()})
    citys = r.html.xpath('//tr[@class="citytr"]')
    for i in citys:
        code = i.xpath('//td[1]/a/text() | //td[1]/text()')[0]
        u = i.xpath('//td[2]/a/@href')
        if u:
            u = urljoin(url, u[0])
            get_county(u, code)
        text = i.xpath('//td[2]/a/text() | //td[2]/text()')[0]
        print(code, u, text)
        save_to_mysql((code, text, parent_code))


def get_county(url, parent_code):
    r = session.get(url, headers={'user-agent': user_agent.generate_user_agent()})
    counties = r.html.xpath('//tr[@class="countytr"]')
    for i in counties:
        code = i.xpath('//td[1]/a/text() | //td[1]/text()')[0]
        u = i.xpath('//td[2]/a/@href')
        if u:
            u = urljoin(url, u[0])
            get_town(u, code)
        text = i.xpath('//td[2]/a/text() | //td[2]/text()')[0]
        print(code, u, text)
        save_to_mysql((code, text, parent_code))


def get_town(url, parent_code):
    r = session.get(url, headers={'user-agent': user_agent.generate_user_agent()})
    counties = r.html.xpath('//tr[@class="towntr"]')
    for i in counties:
        code = i.xpath('//td[1]/a/text() | //td[1]/text()')[0]
        u = i.xpath('//td[2]/a/@href')
        if u:
            u = urljoin(url, u[0])
            get_village(u, code)
        text = i.xpath('//td[2]/a/text() | //td[2]/text()')[0]
        print(code, u, text)
        save_to_mysql((code, text, parent_code))


def get_village(url, parent_code):
    # time.sleep(0.1)
    r = session.get(url, headers={'user-agent': user_agent.generate_user_agent()})
    counties = r.html.xpath('//tr[@class="villagetr"]')
    for i in counties:
        code = i.xpath('//td[1]/text()')[0]
        text = i.xpath('//td[3]/text()')[0]
        print(code, text)
        save_to_mysql((code, text, parent_code))

def transfer_data():
    sql = 'SELECT * FROM zd_area2'
    sql2 = 'INSERT INTO zd_area2 (BM,MC,SJBM) values (%s,%s,%s)'
    cursor = connection.cursor()
    cursor2 = connection2.cursor()

    cursor.execute(sql)
    counter = 1
    while True:
        print('counter: ', counter)
        result = cursor.fetchone()

        if result:
            bm = result['bm']
            mc = result['mc']
            sjbm = result['sjbm']
            cursor2.execute(sql2, (bm,mc,sjbm))
            connection2.commit()
            counter += 1
        else:
            break




if __name__ == '__main__':
    transfer_data()
