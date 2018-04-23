#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/13


import pymysql
import xlrd

MYSQL_CONFIG = {
    'host': '47.93.232.8',
    'port': 3306,
    'user': 'root',
    'passwd': 'FUCKu#0x1024@JSX',
    'db': 'dedecmsv57utf8sp3',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}
TYPES = {'大数据': 5, '新闻': 2, '移动开发': 24, 'AI': 10, '数据库': 11, '其他': 12, '网络': 13, '系统': 14,
         '前端开发': 19, '后端开发': 20}

items = []
def get_data():
    conn = pymysql.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    for typename, typeid in TYPES.items():
        sql = 'select * from dede_archives where  typeid=%s limit 2000'
        cursor.execute(sql, args=(typeid))
        result = cursor.fetchall()
        print(result)

def get_data_from_xlsx():
    pass