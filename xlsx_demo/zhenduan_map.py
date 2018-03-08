#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/5


import xlrd
import xlwt
import re

f = '/Users/yaochao/Downloads/吉林_his_诊断.xlsx'
symbols = ['.', '-', '和', '，', ',', '、', '/', ' ', '或', '[', '伴']


def get_all_values(f, sheet, index):
    hook = xlrd.open_workbook(filename=f)
    sheet = hook.sheet_by_index(sheet)
    col_values = sheet.col_values(index)
    return col_values


def get_all_symbol():
    r = []
    col_values = get_all_values(f, 0, 0)
    print(len(col_values))
    for i in col_values:
        i = str(i)
        i = i.strip()
        for s in symbols:
            if s in i:
                r.append(i)

    return r


def split_N_words():
    r = get_all_symbol()
    for idx, i in enumerate(r):
        pattern = r'{}+'.format('-')
        print(re.sub(pattern, 'yaochao', i))


def write_to_xls(out_path='out.xls'):
    book = xlwt.Workbook(encoding='utf8')
    sheet1 = book.add_sheet(sheetname='sheet1')
    r = get_all_symbol()
    for idx, i in enumerate(r):
        sheet1.write(idx, 0, i)
    book.save(out_path)


def main():
    split_N_words()


if __name__ == '__main__':
    main()
