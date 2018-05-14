#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/9


import requests


def login(username, password):
    '''
    启奥系统 - 登录接口
    :param username:
    :param password:
    :return: requests.session object with login cookie info
    '''
    try:
        s = requests.session()
        response = s.post(
            url="http://jkda.xamwjw.gov.cn/j_spring_security_check",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://jkda.xamwjw.gov.cn/login.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "jsonResult": "true",
                "j_username": username,
                "j_password": password,
            },
        )
        r = response.json()
        print(r)
        if r['loginResult']['result']:
            return s
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


if __name__ == '__main__':
    print(login('hanbomin', '111111'))
