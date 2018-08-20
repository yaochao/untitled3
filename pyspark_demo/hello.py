#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/14


import json
import sys


def transfer(j):
    d = json.loads(j)
    for k, v in d.items():
        if k == '' and v == '':
            return None
    return d


for line in sys.stdin:
    line = line.strip()
    gid, gender, phone, animal_star, payload, ds, appid = line.split('\t')
    gid = None if gid == '' else gid
    gender = None if gender == '' else gender
    phone = None if phone == '' else phone
    animal_star = None if animal_star == '' else animal_star
    payload = None if payload == '' else payload
    ds = None if ds == '' else ds
    appid = None if appid == '' else appid
    payload = str(transfer(payload)).replace(',', '^B').replace(':', '^C')
    print('^I'.join([gid, gender, phone, animal_star, payload, ds, appid]))
