#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2022/1/24


import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'infoxmed',
    'user': 'yaochao',
    'password': 'BYLAo1GKdpQpWdUP!',
    'charset': 'utf8'
}


def get_connect():
    connect = pymysql.connect(**config)
