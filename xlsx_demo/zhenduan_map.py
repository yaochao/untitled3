#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/5


import xlrd
import xlwt
import re
import csv

f = '/Users/yaochao/work/诊断名称/吉林_his_诊断.xlsx'
online_f = '/Users/yaochao/work/诊断名称/online.csv'
# 词表
online_icd_mesh = '/Users/yaochao/python/datasets/user_dicts/online_and_icd_and_mesh.txt'

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
    r'\w+(伴)[^有]\w+',
    r'\w+[^合](并)[^发证]\w+',
]


# 算法改进记录：1.删除 '和'，'或'，'伴有'。2.切分后长度大于三个的忽略切分。3. 带有"(+)","(-)"的不分割(阳性阴性)。


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


def get_all_values_text(f):
    with open(f, encoding='utf-8') as f:
        lines = f.readlines()
        return lines


col_values = get_all_values_xlsx(f, 0, 0)
col_values = [str(x).strip() for x in col_values]
col_values = list(set(col_values))

csv_values = get_all_values_csv(online_f)
csv_values = [str(x[0]).strip() for x in csv_values]

text_values = get_all_values_text(online_icd_mesh)
text_values = [x.strip() for x in text_values]


def get_all_split_name():
    '''
    将所有的name进行分割
    :return:
    '''
    all_items = []
    for i in col_values:
        item = []
        item.append(0)
        item.append(i)
        flag_names = get_split_name(i)
        if not flag_names:
            continue
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
    # 如果name在线上ICD里面，就不分割
    if name in csv_values:
        return
    # 如果name含有'(-)'或者'(+)'，就不分割
    if '(-)' in name or '(+)' in name or '（-）' in name or '（+）' in name:
        return

    for s in symbols_re:
        result = re.findall(s, name)
        if result:
            # 当按照空格分割时，如果去掉空格，在词表中能找到，就不分割：例如"前列腺 炎"
            if s == r'\w+( {1,})\w+':
                tmp = name.replace(' ', '')
                if tmp in text_values:
                    print(name, tmp)
                    return
            flag = result[0]
            names = name.split(flag)
            # 如果分割出来的name不是2个，就不分割
            if len(names) != 2:
                return
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
    book.save('诊断名称处理结果_类型排序_删除线上icd_算法改进.xls')


def test():
    '''
    数据来源是合理用药数据，来测试本功能对合理用药的影响
    :return:
    '''
    file1 = '/Users/yaochao/work/诊断名称/诊疗无结果请求.csv'
    file11 = '/Users/yaochao/work/诊断名称/诊疗无结果请求_诊断分词.csv'
    file2 = '/Users/yaochao/work/诊断名称/诊疗有结果请求.csv'
    file22 = '/Users/yaochao/work/诊断名称/诊疗有结果请求_诊断分词.csv'
    with open(file1, encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        content = list(csv_reader)
        for idx, i in enumerate(content):
            if i[3] == '诊断':
                origin_names = i[4:]
                new_names = []
                for name in origin_names:
                    r = get_split_name(name)
                    if not r:
                        continue
                    new_names += r[1]
                    new_i = i[:4] + new_names
                    # 把原来的i替换为new_i
                    content.pop(idx)
                    content.insert(idx, new_i)
                    print(new_i)

        # # 写进新的csv
        # with open(file11, 'w', encoding='utf-8') as f:
        #     csv_writer = csv.writer(f)
        #     csv_writer.writerows(content)


def main():
    write_to_xls()


if __name__ == '__main__':
    main()
