# !/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/17

'''
this file contains the utils, snippets, gists
I collected it anywhere anyone...
That's all.
'''

##########################################
import sys

import re

if sys.version_info[0] >= 3:
    unicode = str


def any2utf8(text, errors='strict', encoding='utf8'):
    """
    Convert a string (unicode or bytestring in `encoding`), to bytestring in utf8.
    """
    if isinstance(text, unicode):
        return text.encode('utf8')
    # do bytestring -> unicode -> utf8 full circle, to ensure valid utf8
    return unicode(text, encoding, errors=errors).encode('utf8')


##########################################
def cut_sentence(text):
    '''
    中文分句
    :param text:要分句的文本
    :return:分句列表
    '''
    sentences = []
    line = ''
    for char in text:
        if char in '。！？.!?':
            line += char
            sentences.append(line)
            line = ''
        else:
            line += char
    return sentences


def cut_sentence_re(text):
    '''
    中文分句
    :param text:要分句的文本
    :return:分句列表
    '''
    SPLIT_SENTENCES = re.compile("[。！？.!?]")
    sentences = SPLIT_SENTENCES.split(text)
    return sentences
