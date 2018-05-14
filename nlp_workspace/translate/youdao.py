#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/3


import requests
import hashlib
from urllib.parse import quote
import random

APP_KEY = '215128c625d9edc6'
SECRET_KEY = 'UbAIP8JXaPEQU2PtCrkmfZfET2tEa19N'
FROM = 'EN'
TO = 'zh-CHS'


def get_sign(q, salt):
    '''
    获得sign，签名，通过md5(appKey+q+salt+应用密钥)生成
    :return:
    '''
    s = APP_KEY + q + salt + SECRET_KEY
    m = hashlib.md5(s.encode()).hexdigest()
    return m


def main(q):
    salt = str(random.randint(1, 65536))
    sign = get_sign(q, salt)

    rquest_url = 'https://openapi.youdao.com/api'
    response = requests.get(rquest_url, params={
        'q': quote(q),
        'from': FROM,
        'to': TO,
        'appKey': APP_KEY,
        'salt': salt,
        'sign': sign})
    if response.status_code == 200:
        r = response.json()
        if r['errorCode'] == '0':
            translation = r['translation']
            if translation:
                print(translation[0])


if __name__ == '__main__':
    q = '''
    hello, what's your name?
    '''
    main(q)
