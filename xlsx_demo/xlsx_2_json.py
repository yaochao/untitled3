#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/9/27


import csv
import json

FILE_PATH = '/Users/yaochao/work/大象中医/医案/0927dxzy_yian.csv'

def main():

    with open(FILE_PATH, encoding='GBK') as f:
        items = []
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            item = {
                'id': row[0],
                'chaodai': row[1],
                'zhaiyao': row[2],
                'chuchu': row[3],
                'yishi': row[4],
                'bingming': row[5],
                'yianxiangqing': row[6]
            }
            items.append(item)
        # 输出json
        content = {'content': items}
        with open('dxzy_yian.json', 'w') as f:
            f.write(str(content))

if __name__ == '__main__':
    main()