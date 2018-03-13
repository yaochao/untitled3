#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/13


import csv

items = []
items.append(['', '药名','药物1', '药物2','等级','详细信息'])
with open('/Users/yaochao/work/药物相互作用/药与药相互作用_micromedex.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader)
    rows = list(csv_reader)
    for row in rows:
        try:
            item = []
            item.append(row[1][1])
            drug1 = row[2].split('--')[0]
            drug2 = row[2].split('--')[1]
            item.append(drug1)
            item.append(drug2)
            item.append(drug2)
            item.append(row[3][1:])
            item.append(row[4])
            items.append(item)
        except:
            item = []
            item.append(row[1][1])
            drug1 = row[2].split('-')[0]
            drug2 = row[2].split('-')[1]
            item.append(drug1)
            item.append(drug2)
            item.append(drug2)
            item.append(row[3][1:])
            item.append(row[4])
            items.append(item)


with open('/Users/yaochao/work/药物相互作用/药与药相互作用_micromedex2.csv', mode='w', encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(items)