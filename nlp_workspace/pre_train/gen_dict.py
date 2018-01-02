#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/1/2

import csv
import xlrd



def online_and_icd_dict():
    # 生成线上icd词典和标准icd10词典
    icd = '/Users/yaochao/Desktop/work_files/work2/ICD.xls'
    online = '/Users/yaochao/Desktop/work_files/work2/online.csv'

    # csv
    csv_reader = csv.reader(open(online, 'r', encoding='utf-8'))
    online = [x for x in csv_reader][1:]
    online_mc = [x[0] for x in online]

    # xlrd
    icd = xlrd.open_workbook(icd)
    sheet = icd.sheet_by_index(1)
    icd_mc = sheet.col_values(1)[1:]

    print(len(online_mc))
    print(len(icd_mc))
    print(len(icd_mc) + len(online_mc))

    # 合并到一起
    online_mc.extend(icd_mc)
    online_mc = set(online_mc)
    print(len(online_mc))
    online_mc = [word + '\n' for word in online_mc]
    # 写入txt
    with open('online_and_icd.txt', 'w', encoding='utf-8') as f:
        f.writelines(online_mc)



def online_and_icd_and_mesh_dict():
    icd = '/Users/yaochao/Desktop/work_files/work2/ICD.xls'
    online = '/Users/yaochao/Desktop/work_files/work2/online.csv'

    # csv
    csv_reader = csv.reader(open(online, 'r', encoding='utf-8'))
    online = [x for x in csv_reader][1:]
    online_mc = [x[0] for x in online]

    # xlrd
    icd = xlrd.open_workbook(icd)
    sheet = icd.sheet_by_index(1)
    icd_mc = sheet.col_values(1)[1:]

    # mesh 疾病
    with open('/Users/yaochao/python/datasets/user_dicts/wf_jb_dict_full.txt', encoding='utf-8') as f:
        jb = f.readlines()
        jb = [word[:-1] for word in jb]
        print(len(jb))
    # mesh 解剖学
    with open('/Users/yaochao/python/datasets/user_dicts/wf_jpx_dict_full.txt', encoding='utf-8') as f:
        jpx = f.readlines()
        jpx = [word[:-1] for word in jpx]
        print(len(jpx))


    print(len(online_mc))
    print(len(icd_mc))
    print(len(icd_mc) + len(online_mc) + len(jb) + len(jpx))

    # # 合并到一起
    online_mc.extend(icd_mc)
    online_mc.extend(jb)
    online_mc.extend(jpx)
    online_mc = set(online_mc)
    print(len(online_mc))
    online_mc = [word + '\n' for word in online_mc]
    # 写入txt
    with open('online_and_icd_and_mesh.txt', 'w', encoding='utf-8') as f:
        f.writelines(online_mc)

if __name__ == '__main__':
    online_and_icd_and_mesh_dict()