#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/27


# 挑选出csv中含有血压的列表

import csv

items = []
with open('诊疗无结果请求.csv', encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    f_csv = list(f_csv)
    for i in range(0, len(f_csv), 7):
        item = f_csv[i: i + 7]
        for ii in item[5][3:]:
            if '血压' in ii:
                items.append(item)

print(len(items))
with open('诊疗无结果请求_血压.csv', mode='w', encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['id', '人员', '', '字段名'])
    for item in items:
        f_csv.writerows(item)
