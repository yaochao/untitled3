#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/6


from mini_spider.base.downloader import Downloader
from mini_spider.base.parser import Parser
import pprint

start_url = 'http://www.sothebys.com/en/auctions/2018/the-otto-naumann-sale-n09810.html'

downloader = Downloader(url=start_url, is_ajax=True)
html = downloader.html
pprint.pprint(html)

# parser = Parser(xpath='//ul[@class="feed_ul"]/li/div/a/div[2]/h3/text()', html=html)
# pprint.pprint(parser.parse())