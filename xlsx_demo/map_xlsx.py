#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/1/30


import xlrd
import xlwt

base = '/Users/yaochao/Downloads/'
p1 = base + '1.xlsx'
p2 = base + '2.xlsx'

p2 = xlrd.open_workbook(p2)
sheet = p2.sheet_by_index(0)
type_id = sheet.col_values(0)
type_name = sheet.col_values(1)
map_dict = {}
for index, i in enumerate(type_id):
    map_dict[i] = type_name[index]

print(map_dict)

p1 = xlrd.open_workbook(p1)
sheet = p1.sheet_by_index(0)
type_id = sheet.col_values(1)

workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet('sheet1')
for index, i in enumerate(type_id[1:]):
    # sheet1.write(index, 0, map_dict[i])
    print(map_dict[i])

workbook.save('map.xlsx')
