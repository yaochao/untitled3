#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/19


import csv


def get_values_csv(path):
    with open(path, encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
        body = list(csv_reader)
        return header, body


def write_values_csv(path, header=None, body=None):
    with open(path, mode='w', encoding='utf-8') as f:
        f_writer = csv.writer(f)
        if header:
            f_writer.writerow(header)
        if body:
            f_writer.writerows(body)


def compare_csvs():
    header1, body1 = get_values_csv('/Users/yaochao/work/compare_csvs/诊疗返回值.csv')
    header2, body2 = get_values_csv('/Users/yaochao/work/compare_csvs/诊疗返回值切词前第三次.csv')

    equal_ids = set()
    for i in body1:
        for ii in body2:
            if i[:2] == ii[1:3]:
                # print(i[:2])
                # print(ii[1:3])
                # print('*********************************')
                equal_ids.add(i[0])
    return equal_ids


def main():
    ids = compare_csvs()
    print(ids)
    ids = [[x] for x in ids]
    write_values_csv('equal_ids.csv', body=list(ids))


if __name__ == '__main__':
    main()
