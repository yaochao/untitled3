#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/1/30


import xlrd
import xlwt
import csv

base = '/Users/yaochao/Downloads/'
p1 = base + '返回值施楠楠.xlsx'
p2 = base + '诊疗返回值20180105.xlsx'

p1 = xlrd.open_workbook(p1)
sheet = p1.sheet_by_index(0)
type_id = sheet.col_values(1)


p2 = xlrd.open_workbook(p2)
sheet2 = p2.sheet_by_index(0)
type_id2 = sheet2.col_values(3)


for index, i in enumerate(type_id2[1:]):
    if i in type_id:
        print(1)
    else:
        print(2)

