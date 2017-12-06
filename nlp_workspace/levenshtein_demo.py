#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/10


import Levenshtein
import xlrd
import xlwt
import csv

f1 = '/Users/yaochao/Desktop/work_files/ICD-10-v6.01.xls'
f2 = '/Users/yaochao/Desktop/work_files/illness_total.xlsx'

# xls reader
data1 = xlrd.open_workbook(f1)
data2 = xlrd.open_workbook(f2)

table1 = data1.sheet_by_index(1)
table2 = data2.sheet_by_index(0)

cols1 = table1.col_values(1)
cols2 = table2.col_values(1)

# xls writer
workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet('sheet1')
sheet1.write(0, 0, 'id')
sheet1.write(0, 1, 'illness_name')
sheet1.write(0, 2, '推荐1')
sheet1.write(0, 3, '推荐2')
sheet1.write(0, 4, '推荐3')

# csv writer
f = open('illness_haodf.csv', 'w', encoding='utf8')
writer = csv.writer(f)
writer.writerow(['id', 'illness_name', '推荐1', '推荐2', '推荐3'])

for index1, i in enumerate(cols2[1:], 1):
    distances = []
    for index2, ii in enumerate(cols1[1:], 1):
        distance = Levenshtein.distance(i, ii)
        distances.append([distance, index2])
    distances.sort()
    if distances[0][0] == 0:
        distances = [distances[0]]
    else:
        distances = distances[0:3]
    distances = [cols1[x[1]] for x in distances]

    # write to xls
    sheet1.write(index1, 0, str(index1))
    sheet1.write(index1, 1, cols2[index1])
    for index3, illness in enumerate(distances):
        sheet1.write(index1, 2 + index3, illness)

    # write to csv
    data = [str(index1), cols2[index1]] + distances
    writer.writerow(data)

    print(index1)

workbook.save('illness_haodf.xls')
