#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/6


from mini_spider.base.downloader import Downloader

start_url = 'https://www.so.com/'

downloader = Downloader(url=start_url)
html = downloader.html
print(html)