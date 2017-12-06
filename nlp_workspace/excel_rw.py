#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/10


import xlrd

data = xlrd.open_workbook('/Users/yaochao/Desktop/work_files/ICD-10 v6.01版.xls')
table = data.sheet_by_index(1)
cols = table.col_values(1)
dics = ' '.join(cols)
with open('dicts_illness.txt', 'wb') as f:
    f.write(dics.encode('utf8'))