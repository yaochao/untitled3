#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/1/6
import csv
import jieba
from functools import reduce
import xlrd
import csv

path = '/Users/yaochao/python/datasets/stopwords/'
icd = '/Users/yaochao/Desktop/work_files/work2/ICD.xls'
online = '/Users/yaochao/Desktop/work_files/work2/online.csv'
# online
csv_reader = csv.reader(open(online, 'r', encoding='utf-8'))
online_words = [x[0] for x in csv_reader][1:]
# icd10标准表
icd = xlrd.open_workbook(icd)
sheet = icd.sheet_by_index(1)
icd_words = sheet.col_values(1)[1:]


def test_stopwords():
    a = []
    with open(path + 'stopwords5.txt', encoding='utf-8') as f:
        stopwords = f.readlines()
        stopwords = [x.split('\n')[0] for x in stopwords]
    for i in online_words:
        i_cut = jieba.cut(i)
        for cut in i_cut:
            if cut in stopwords:
                a.append(cut)

    for i in icd_words:
        i_cut = jieba.cut(i)
        for cut in i_cut:
            if cut in stopwords:
                a.append(cut)


    aa = []
    for i in set(a):
        aa.append([i, a.count(i)])
    aa.sort(key=lambda x:x[1],reverse=True)
    print(aa)

    with open('stopwords_count3.csv', 'w', encoding='utf-8') as f:
        csv_w = csv.writer(f)
        csv_w.writerow(('word', 'count', 'word1', 'word2', 'word3', 'word4', 'word5'))
        # [csv_w.writerow(i) for i in aa]
        for i in aa:
            word = i[0]
            tmp = set()
            for ii in icd_words:
                ii_cut = jieba.cut(ii)
                if word in ii_cut:
                    tmp.add(ii)
                    if len(tmp) >= 5:
                        break
            if len(tmp) < 5:
                for iii in online_words:
                    iii_cut = jieba.cut(iii)
                    if word in iii_cut:
                        tmp.add(iii)
                        if len(tmp) >= 5:
                            break
            i.extend(list(tmp))
            csv_w.writerow(i)


if __name__ == '__main__':
    test_stopwords()
