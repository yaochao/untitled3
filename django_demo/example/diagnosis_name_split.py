#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/5


import re
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
online_f = os.path.join(BASE_DIR, 'misc/online.csv')
# 词表
online_icd_mesh = os.path.join(BASE_DIR, 'misc/online_and_icd_and_mesh.txt')
online_icd_mesh_jilincibiao = os.path.join(BASE_DIR, 'misc/online_and_icd_and_mesh_吉林词表.txt')
jilin_cibiao = os.path.join(BASE_DIR, 'misc/吉林_his_诊断_词表.txt')

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


def get_all_values_text(f):
    with open(f, encoding='utf-8') as f:
        lines = f.readlines()
        return lines


csv_values = get_all_values_csv(online_f)
csv_values = [str(x[0]).strip() for x in csv_values]

text_values = get_all_values_text(online_icd_mesh_jilincibiao)
text_values = [x.strip() for x in text_values]

jilin_cibiao = get_all_values_text(jilin_cibiao)
jilin_cibiao = [x.strip() for x in jilin_cibiao]


def get_all_split_name(names):
    '''
    将所有的name进行分割
    :return:
    '''
    all_items = {}
    for name in names:
        r = get_split_name(name)
        all_items[name] = r if r else [name]

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
    # 如果name在自定义的词表里面，就不分割
    if name in jilin_cibiao:
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
                    print(name, '===', tmp)
                    return
            flag = result[0]
            names = name.split(flag)
            # 如果分割出来的name不是2个，就不分割
            if len(names) != 2:
                return
            print(name, ':', names)
            return names


def main():
    names = ['糖尿病，高血压', '冠心病', '脑梗--脑残']
    print(get_all_split_name(names))


if __name__ == '__main__':
    main()
