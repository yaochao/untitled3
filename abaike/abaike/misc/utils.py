#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/28


from readability import Document
from scrapy import Selector

def get_summary(content):
    doc = Document(content)
    summary = doc.summary(html_partial=True)
    return summary

def get_text(content):
    html = get_summary(content)
    content_text = Selector(text=html).xpath('string(.)').extract_first()
    content_text = content_text.strip().replace('\r', '').replace('\n', '').replace('\t', '')
    return content_text