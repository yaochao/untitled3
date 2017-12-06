#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by yaochao at 2017/10/17


import csv
import xlwt
import xlrd

icd = '/Users/yaochao/Desktop/work_files/work2/ICD.xls'
online = '/Users/yaochao/Desktop/work_files/work2/online.csv'
result = '/Users/yaochao/Desktop/work_files/work2/result.xlsx'

# csv
csv_reader = csv.reader(open(online, 'r', encoding='utf-8'))
online = [x for x in csv_reader][1:]
online_mc = [x[0] for x in online]
online_bm = [x[1] for x in online]
online_bm = [x.split('.')[0] for x in online_bm]

# xlrd
icd = xlrd.open_workbook(icd)
sheet = icd.sheet_by_index(1)
icd_mc = sheet.col_values(1)[1:]
icd_bm = sheet.col_values(2)[1:]
icd_bm = [x[0:3] for x in icd_bm]


# xlrd
result = xlrd.open_workbook(result)
sheet = result.sheet_by_index(0)
bm_range = sheet.col_values(1)[3:]
bm_range = [[str.upper(x.split('-')[0]), str.upper(x.split('-')[1])] for x in bm_range]


# 生成所有的范围内的字符串
def count_bm(start='A01', stop='A98'):
    # 存放在给定范围的编码的两个数组
    online_in_range_total = 0
    icd_in_range_total = 0

    start_prefix = start[0]
    start_suffix = int(start[1:3])
    stop_prefix = stop[0]
    stop_suffix = int(stop[1:3])
    start_prefix = ord(start_prefix)
    stop_prefix = ord(stop_prefix)
    for prefix in range(start_prefix, stop_prefix + 1):
        for suffix in range(0, 100):
            # 去掉不在范围内的
            if prefix == start_prefix:
                if suffix < start_suffix:
                    continue
            if prefix == stop_prefix:
                if suffix > stop_suffix:
                    continue
            suffix = '0%s' % suffix if suffix < 10 else '%s' % suffix  # 小于10的转换为01-09两位数字符串，大于10的转换为字符串
            prefix_suffix = chr(prefix) + suffix
            for bm in online_bm:
                if bm == prefix_suffix:
                    online_in_range_total += 1
            for bm in icd_bm:
                if bm == prefix_suffix:
                    icd_in_range_total += 1

    return online_in_range_total, icd_in_range_total


def gogogo():
    online_total = 0
    icd_total = 0

    for index, i in enumerate(bm_range):
        online_in_range, icd_in_range = count_bm(start=i[0], stop=i[1])
        print(index + 4, icd_in_range, online_in_range)
        online_total += online_in_range
        icd_total += icd_in_range
    print(online_total)
    print(icd_total)


gogogo()
