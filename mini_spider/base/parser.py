#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/6


from lxml import etree

class Parser:

    def __init__(self, xpath, html):
        self.xpath = xpath
        self.html = html

    def parse(self):
        tree = etree.HTML(self.html)
        return tree.xpath(self.xpath)