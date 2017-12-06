#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/11/17


import xlrd


def split_jiepaocibiao():
    body_names = []
    jiepaocibiao = '/Users/yaochao/Desktop/work_files/cibiao/jiepaocibiao.xlsx'
    workbook = xlrd.open_workbook(jiepaocibiao)
    sheet = workbook.sheet_by_name(sheet_name='Sheet1')
    names = sheet.col_values(colx=0)
    for name in names:
        names = name.split('-')
        body_names = body_names + names
    body_names = set(body_names)
    body_names.remove('')
    return body_names


body_names = split_jiepaocibiao()
with open('jiepaocibiao.txt', 'w', encoding='utf-8') as f:
    for name in body_names:
        f.write(name + '\n')
