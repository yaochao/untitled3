#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/6


from mini_spider.base.downloader import Downloader
import pprint

start_url = 'http://36kr.com/'

downloader = Downloader(url=start_url, is_ajax=False)
html = downloader.html
pprint.pprint(html)