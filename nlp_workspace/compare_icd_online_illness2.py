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
sheet1 = workbook.add_sheet('sheet1')
sheet1.write(0, 0, 'v6.01中文名称')
sheet1.write(0, 1, 'v6.01编码')
sheet1.write(0, 2, '线上库中文名称')
sheet1.write(0, 3, '线上库编码')
sheet1.write(0, 4, '1.完全一致 2.编码不一致 3.都不一致')

# online和icd的名称和编码都相同
same_mc_same_bm = []
for index1, i in enumerate(online):
    for ii in icd:
        if i == ii:
            ol_mc = i[0]
            ol_bm = i[1]
            icd_mc = ii[0]
            icd_bm = ii[1]
            row = len(same_mc_same_bm) + 1
            sheet1.write(row, 0, icd_mc)
            sheet1.write(row, 1, icd_bm)
            sheet1.write(row, 2, ol_mc)
            sheet1.write(row, 3, ol_bm)
            sheet1.write(row, 4, 1)
            # print(i, ii, ' same_mc_same_bm')
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
            row = len(same_mc_same_bm) + 1 + len(same_mc_not_bm) + 1
            sheet1.write(row, 0, icd_mc)
            sheet1.write(row, 1, icd_bm)
            sheet1.write(row, 2, ol_mc)
            sheet1.write(row, 3, ol_bm)
            sheet1.write(row, 4, 2)
            # print(i, ii, ' same_mc_not_bm')
            same_mc_not_bm.append([i, ii])

# online和icd的名称不相同，编码不相同，通过编辑距离，给online找一个最相近的IDC的名称。
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
row = len(same_mc_same_bm) + 1 + len(same_mc_not_bm) + 1 + 4
sheet1.write(row, 0, '线上库中文名称')
sheet1.write(row, 1, '身体部位')
sheet1.write(row, 2, '剩下的字')
sheet1.write(row, 3, '疾病名称')
sheet1.write(row, 4, '剩下的字')

for index, i in enumerate(online):
    ol_mc = i[0]
    ol_bm = i[1]
    word, bodys, tmp_word, illnesses, tmp_word2 = get_body_illness2(ol_mc)

    row1 = row + index + 1

    sheet1.write(row1, 0, word)
    sheet1.write(row1, 1, bodys)
    sheet1.write(row1, 2, tmp_word)
    sheet1.write(row1, 3, illnesses)
    sheet1.write(row1, 4, tmp_word2)

workbook.save('fenci_demo.xls')

used_time = time.time() - start_time
print('used_time: {}'.format(used_time))
