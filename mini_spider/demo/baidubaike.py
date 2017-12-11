#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/8


import requests
import cchardet
from urllib.parse import urljoin
from lxml import etree

def downloader(url=''):
    '''
    下载器: 把网页源代码下载下来
    '''
    response = requests.get(url, headers={'User-Agent': 'baiduspider'})
    content = response.content
    text = content.decode(cchardet.detect(content)['encoding'])
    return text



def parser(html):
    '''
    解析器: 解析出网页中，我们想要的东西
    '''
    urls = []
    titles = []
    tree = etree.HTML(html)
    tags = tree.xpath('//a')
    for tag in tags:
        url = tag.xpath('@href')
        url = url[0] if len(url) > 0 else ''
        title = tag.xpath('text()')
        title = title[0] if len(title) > 0 else ''

        if url and url.startswith('/item/') and title:
            url = urljoin('https://baike.baidu.com', url)
            urls.append(url)
            titles.append(title)
    return urls, titles


def pipeline(all_titles):
    '''
    数据管道（保存数据，输出数据）
    '''
    for i in all_titles:
        print(i)


def dispatcher():
    '''
    调度器: 让这个程序活起来
    '''
    new_urls = set()
    old_urls = set()
    all_titles = []
    flag = 0
    new_urls.add('https://baike.baidu.com/item/Python/407313')

    while len(new_urls) > 0:
        # 这边控制只抓100个网页，可以修改任意值
        if flag >= 100:
            break

        url = new_urls.pop()
        print(url)
        # 1. 下载
        html = downloader(url)
        # 2. 解析
        urls, titles = parser(html=html)
        new_urls = new_urls.union(set(urls))
        all_titles = all_titles + titles
        old_urls.add(url)
        flag = flag + 1

    # 3. 把解析出来的数据放到管道里
    pipeline(all_titles)

# 运行我的程序，这里是程序入口
if __name__ == '__main__':
    dispatcher()