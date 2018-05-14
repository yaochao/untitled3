#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/9
import pymysql

from .qiao_login import login

__all__ = ['login', 'LoginTimeoutException', 'MYSQL_CONF_LOCAL', 'MYSQL_CONF_DEV', 'MONGO_CONF']

MYSQL_CONF_LOCAL = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'toor',
    'db': 'work',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

MYSQL_CONF_DEV = {
    'host': '127.0.0.1',
    'port': 8891,
    'user': 'phstest',
    'passwd': 'phstest@20161205',
    'db': 'g_lb',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

MONGO_CONF = {
    'host': '127.0.0.1',
    'port': 27017,
}

user_pass_list = [
    ('科右中旗卫生局', 'xingjinhua', '123456789'),
    ('巴彦呼舒镇社区卫生服务中心','152222001','111111'),
    ('吐列毛杜','cyl','cyl537'),
    ('高力板','Wxp','19751231'),
    ('巴彦淖尔','ysg','yu2008li'),
    ('杜尔基','hanbomin','111111'),
    ('好腰苏木','220150001','hbx18704864999'),
    ('新佳木','licheng','111111'),
    ('代钦塔拉','liuch','654321'),
    ('巴仁哲里木','mhj','123456'),
    ('坤都冷','lfx111','13654827241'),
    ('巴彦忙哈','hanguolin','010203'),
    ('西日嘎','tjs','111111'),
    ('巴仁太本','gaochangsui','654321'),
    ('义和道卜','gwh1','13948224598'),
    ('布敦化','baifengying','27145156'),
    ('准太本','kxy','111111'),
    ('巴扎拉嘎','suliyun','sly123'),
    ('额木庭高勒','bty','1234567'),
    ('哈日诺尔','baohaimei','222222'),
    ('扎木沁','jinlong','123456789'),
    ('吐列毛杜农场','daixiaorong','123123123'),
    ('布敦化牧场','wbl','wbl123456'),
    ('铜矿','zhengjing','668800'),
    ('孟恩套力盖银铅矿职工医院','qkjfy','BNM291'),
]


class LoginTimeoutException(Exception):
    def __init__(self, msg):
        self.msg = msg


