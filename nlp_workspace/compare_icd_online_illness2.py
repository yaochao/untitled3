#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/17


import csv
import xlwt
import xlrd
import Levenshtein
import time
from nlp_workspace.fenci_demo import get_body_illness2

start_time = time.time()

icd = '/Users/yaochao/Desktop/work_files/work2/ICD.xls'
online = '/Users/yaochao/Desktop/work_files/work2/online.csv'
result = '/Users/yaochao/Desktop/work_files/work2/result2.xlsx'

# csv
csv_reader = csv.reader(open(online, 'r', encoding='utf-8'))
online = [x for x in csv_reader][1:]
online_mc = [x[0] for x in online]
online_bm = [x[1] for x in online]

# xlrd
icd = xlrd.open_workbook(icd)
sheet = icd.sheet_by_index(1)
icd_mc = sheet.col_values(1)[1:]
icd_bm = sheet.col_values(2)[1:]
icd = []
for x in range(len(icd_mc)):
    icd.append([icd_mc[x], icd_bm[x]])

# xlwt
workbook = xlwt.Workbook(encoding='utf-8')
wt_sheet1 = workbook.add_sheet('online')
wt_sheet2 = workbook.add_sheet('icd')

# online和icd的名称和编码都相同
same_mc_same_bm = []
for index1, i in enumerate(online):
    for ii in icd:
        if i == ii:
            same_mc_same_bm.append(i)

# online和icd的名称相同，编码不相同
for i in same_mc_same_bm:
    online.remove(i)
    icd.remove(i)

same_mc_not_bm = []

for index, i in enumerate(online):
    for ii in icd:
        ol_mc = i[0]
        ol_bm = i[1]
        icd_mc = ii[0]
        icd_bm = ii[1]
        if ol_mc == icd_mc and ol_bm != icd_bm:
            same_mc_not_bm.append([i, ii])

# online和icd的名称不相同，编码不相同
same_mc_not_bm_online = [x[0] for x in same_mc_not_bm]
same_mc_not_bm_icd = [x[1] for x in same_mc_not_bm]
for i in same_mc_not_bm_online:
    if i not in online:
        print(i, 'not in online')
        continue
    online.remove(i)
for i in same_mc_not_bm_icd:
    if i not in icd:
        print(i, 'not in icd')
        continue
    icd.remove(i)

# with open('remain_online.txt', 'w', encoding='utf-8') as f:
#     f.writelines([x[0] + '\n' for x in online])
#
# with open('remain_icd.txt', 'w', encoding='utf-8') as f:
#     f.writelines([x[0] + '\n' for x in icd])

wt_sheet1.write(0, 0, 'online_name')
wt_sheet1.write(0, 1, 'online_code')
for idx, i in enumerate(online):
    name = i[0]
    code = i[1]
    wt_sheet1.write(idx + 1, 0, name)
    wt_sheet1.write(idx + 1, 1, code)

wt_sheet2.write(0, 0, 'icd_name')
wt_sheet2.write(0, 1, 'icd_code')
for idx2, ii in enumerate(icd):
    name = ii[0]
    code = ii[1]
    wt_sheet2.write(idx2 + 1, 0, name)
    wt_sheet2.write(idx2 + 1, 1, code)

workbook.save('remain_online_icd.xls')
