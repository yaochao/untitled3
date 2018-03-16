#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/16


import requests
import xlrd
import os


def downloader(url, out):
    response = requests.get(url)
    if response.status_code == 200:
        with open(out, 'wb') as f:
            if len(response.content) == int(response.headers['Content-Length']):
                for chunk in response.iter_content():
                    f.write(chunk)
                    return True
    return False


def get_all_values_xlsx(f, sheet, index):
    hook = xlrd.open_workbook(filename=f)
    sheet = hook.sheet_by_index(sheet)
    col_values = sheet.col_values(index)
    return col_values


def main():
    out_path = '/Users/yaochao/Downloads/images/'
    f = '/Users/yaochao/Downloads/imgurls.xlsx'
    urls = get_all_values_xlsx(f, 0, 1)
    for url in urls[1:2]:
        filename = url.split('/')[-1]
        filename = os.path.join(out_path, filename)
        r = downloader(url, out=filename)
        if r:
            print(filename, '下载完成')
        else:
            print(filename, '下载失败')


if __name__ == '__main__':
    main()
