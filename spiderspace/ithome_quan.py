#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2019/1/25


'''
IT之家圈子爬虫
'''
import requests
from lxml.html import etree
import logging
from urllib.parse import urljoin
import pymysql
import time

logger = logging.getLogger(__name__)

params = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'toor',
    'db': 'yaochao',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}
connect = pymysql.connect(**params)
cursor = connect.cursor()


def get_value(tmp):
    if type(tmp) == list:
        return tmp[0] if tmp else ''
    else:
        return tmp


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response


def parse(response):
    if not response: return
    response_url = response.url
    tree = etree.HTML(response.content.decode("utf-8"))
    for i in tree.xpath('//*[@class="t_list"]/ul/li'):
        author_url = i.xpath('div[1]/a/@href')
        author_avatar = i.xpath('div[1]/a/img/@src')

        t_title = i.xpath('div[2]/div[1]')[0]
        post_url = t_title.xpath('a/@href')
        post_title = t_title.xpath('a/text()')

        t_info = i.xpath('div[2]/div[2]')[0]
        author_name = t_info.xpath('a/text()')
        if t_info.xpath('span[1]/a'):
            # 有机型标签
            os_type = t_info.xpath('span[1]/@class')
            device_type = t_info.xpath('span[1]/a/text()')
            post_time = t_info.xpath('span[2]/text()')
        else:
            os_type = ''
            device_type = ''
            post_time = t_info.xpath('span[1]/text()')
        comment_count = t_info.xpath('span[@class="numb"]/text()')
        comment_count = comment_count[0] if comment_count else 0

        result = {
            'author_url': urljoin(response_url, get_value(author_url)),
            'author_avatar': 'http:' + get_value(author_avatar),
            'post_url': urljoin(response_url, get_value(post_url)),
            'post_title': get_value(post_title),
            'author_name': get_value(author_name),
            'os_type': get_value(os_type),
            'device_type': get_value(device_type),
            'post_time': get_value(post_time),
            'comment_count': comment_count
        }
        print(result)
        persistence(result)

def persistence(result):
    sql = 'INSERT INTO ithome_quan (post_title, author_name, device_type, os_type, comment_count, post_url, author_avatar, post_time, author_url) values (%(post_title)s,' \
          '%(author_name)s,%(device_type)s,%(os_type)s,%(comment_count)s,%(post_url)s,%(author_avatar)s,%(post_time)s,%(author_url)s)'
    cursor.execute(sql, result)
    connect.commit()


def main():
    base_url = 'https://quan.ithome.com/talk/'
    for i in range(43, 5000):
        url = base_url + str(i)
        logger.warning('正在抓取:' + url)
        response = get_html(url)
        parse(response)
        logger.warning('保存成功:' + url)
    connect.close()


if __name__ == '__main__':
    main()
