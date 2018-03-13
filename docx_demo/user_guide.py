#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/8


import docx
import os
import re
from execjs_demo.execjs_demo import exec_my_js

base = '/Users/yaochao/work/说明书差异对比和提取'
file1 = os.path.join(base, 'doc_handle1/【JYY编号1】硝苯地平控释片说明书 OCR版-质控后.docx')
file2 = os.path.join(base, 'doc_handle2/【JYY编号1】1.钙拮抗剂-1：[拜新同]硝苯地平控释片（done） 3.docx')
files_name = os.listdir(base)


def get_all_texts():
    files = [os.path.join(base, x) for x in files_name]
    texts = []
    for f in files:
        if '.docx' in f:
            doc = docx.Document(f)
            paragraphs = doc.paragraphs
            text = '\n'.join([x.text for x in paragraphs])
            texts.append(text)
    return texts


def get_text(f):
    doc = docx.Document(f)
    paragraphs = doc.paragraphs
    text = '\n'.join([x.text for x in paragraphs])
    return text


def get_all_titles(texts):
    title_re = r'【.+?】'
    title_re = re.compile(title_re)
    titles = []
    for t in texts:
        r = re.findall(title_re, t)
        titles.extend(r)
    return set(titles)


def get_all_parts(text):
    title_re = '【(.+?)】([\n\w\W]+?)(?<![见和])(?=【|$)'
    parts = re.findall(title_re, text)

    return parts


def main():
    text = get_text(file1)
    parts = get_all_parts(text)
    for part in parts:
        print(part[0])


if __name__ == '__main__':
    main()
