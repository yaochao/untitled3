#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/5


import xlrd
import xlwt
import re
import csv

f = '/Users/yaochao/work/诊断名称/吉林_his_诊断.xlsx'
online_f = '/Users/yaochao/work/诊断名称/online.csv'

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


def get_all_values_xlsx(f, sheet, index):
    hook = xlrd.open_workbook(filename=f)
    sheet = hook.sheet_by_index(sheet)
    col_values = sheet.col_values(index)
    return col_values


col_values = get_all_values_xlsx(f, 0, 0)
col_values = [str(x).strip() for x in col_values]
col_values = list(set(col_values))

csv_values = get_all_values_csv(online_f)
csv_values = [str(x[0]).strip() for x in csv_values]


def get_all_split_name():
    '''
    将所有的name进行分割
    :return:
    '''
    all_items = []
    for i in col_values:
        item = []
        # 给定的疾病名称，是否在线上ICD里面
        if i not in csv_values:
            item.append(0)
            item.append(i)
            flag_names = get_split_name(i)
            if flag_names:
                flag = flag_names[0]
                names = flag_names[1]
                item.append(flag)
                [item.append(name) for name in names]
                all_items.append(item)

    # 对r进行排序，按照分隔符排序
    all_items.sort(key=lambda x: x[2])
    return all_items


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
            return flag, names


def write_to_xls():
    '''
    写到xls中
    :param out_path: 输出路径
    :return:
    '''
    book = xlwt.Workbook(encoding='utf8')
    sheet1 = book.add_sheet(sheetname='sheet1')
    r = get_all_split_name()
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
    book.save('诊断名称处理结果_类型排序_删除线上icd.xls')


def main():
    write_to_xls()


if __name__ == '__main__':
    main()
