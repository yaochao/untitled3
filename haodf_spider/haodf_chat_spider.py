#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/13


import pymysql

MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'haodf_jishux',
    'charset': 'utf8',
}

total = 1217156
connect = pymysql.connect(**MYSQL_CONF)
cursor = connect.cursor()
for x in range(0, 10):
    start = x * 10000 + 1
    stop = (x + 1) * 10000
    print(start - 1, stop)
    # sql = 'SELECT zixun_url from haodf_chats ORDER BY id ASC LIMIT {},{}'.format(start - 1, stop)
    # cursor.execute(sql)
    # result = cursor.fetchall()
    #
    # for url in result:
    #     print(url[0])

cursor.close()
connect.close()
