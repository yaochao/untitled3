#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/5


import xlrd
import xlwt
import re
import csv

f = '/Users/yaochao/Downloads/吉林_his_诊断.xlsx'
online_f = '/Users/yaochao/python/datasets/online_icd/online.csv'
symbols = ['.', '-', '和', '，', ',', '、', '/', ' ', '或', '[', '伴']

symbols_re = [
    r'\w+(-{1,7})\w+',
    r'\w+(，)[^其他的]\w+',  # 继发性肺动脉高压，其他的
    r'\w+(\[\w+\]$)\w+',  # 过敏性鼻炎[变应性鼻炎]        急性鼻咽炎［感冒］      变应性［过敏性］紫癜
    r'\w+(、)\w+',  # 高血压病、脑供血不足
    r'\w+(/)\w+',  # 高血压/冠心病
    r'\w+( {1,})\w+',  # 高血压 脑梗
    r'\w+(,)[^其他的]\w+',  # 高血压病,脑梗
    r'\w+(\.)\w+',  # 不规则流血.尿路感染
    r'\w+(。)\w+',  # 盆腔炎。膀胱炎
    r'\w+(和)\w+',  # 生殖器和泌尿生殖道的疱疹病毒感染
    r'\w+(伴有)\w+',
    r'\w+(伴)\w+',
    r'\w+(或)\w+',
    r'\w+[^合](并)[^发证]\w+',
]


def get_all_values_csv(file_path):
    with open(file_path, encoding='utf-8') as f:
        csv_f = csv.reader(f)
        csv_header = next(csv_f)
        csv_values = list(csv_f)
        return csv_values


def get_all_values(f, sheet, index):
    hook = xlrd.open_workbook(filename=f)
    sheet = hook.sheet_by_index(sheet)
    col_values = sheet.col_values(index)
    return col_values


col_values = get_all_values(f, 0, 0)
col_values = [str(x).strip() for x in col_values]
col_values = list(set(col_values))


def get_all_split_name():
    '''
    将所有的name进行分割
    :return:
    '''
    r = []
    for i in col_values:
        i = str(i).strip()
        names = get_split_name(i)
        if names:
            r.append(names)
            names.insert(0, i)
        # else:
        #     r.append([i, 'null'])
    # 对r进行排序
    r.sort(key=lambda x: x[1])
    return r


def get_split_name(name):
    '''
    找到这个name的一种分割形式
    :param name:
    :return:
    '''
    for s in symbols_re:
        result = re.findall(s, name)
        if result:
            flag = result[0]
            names = name.split(flag)
            names.insert(0, flag)
            return names


def get_all_split_name2():
    '''
    单独的某个分割符的所有结果
    :return:
    '''
    result = []
    for s in symbols_re:
        for i in col_values:
            r = re.findall(s, i)
            if r:
                flag = r[0]
                names = i.split(flag)
                names.insert(0, flag)
                names.insert(0, i)
                result.append(names)
    return result


def is_in_online():
    r = get_all_split_name()
    r2 = get_all_values_csv(online_f)
    r2 = [x[0] for x in r2]
    for idx, i in enumerate(r):
        if i[0] in r2:
            i.insert(0, '1')
        else:
            i.insert(0, '0')
    # 根据0、1进行排序
    r.sort(key=lambda x:x[0])
    return r



def write_to_xls(out_path='诊断名称处理结果_类型排序_是否在线上icd_3.xls'):
    '''
    写到xls中
    :param out_path: 输出路径
    :return:
    '''
    book = xlwt.Workbook(encoding='utf8')
    sheet1 = book.add_sheet(sheetname='sheet1')
    # r = get_all_split_name()
    r = is_in_online()
    # 写表头
    sheet1.write(0, 0, '是否在线上ICD（0为否，1为是）')
    sheet1.write(0, 1, '原诊断名称')
    sheet1.write(0, 2, '分割符')
    sheet1.write(0, 3, '新1')
    sheet1.write(0, 4, '新2')
    sheet1.write(0, 5, '新3')
    sheet1.write(0, 6, '新4')
    # 循环写表内容
    for row, i in enumerate(r):
        for column, ii in enumerate(i):
            sheet1.write(row + 1, column, ii)
    book.save(out_path)


def main():
    write_to_xls()


if __name__ == '__main__':
    main()
