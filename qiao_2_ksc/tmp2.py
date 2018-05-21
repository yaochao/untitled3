#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/21

import requests


def diff_lnr():
    '''
    对比老年人不同的数据
    :return:
    '''
    with open('/Users/yaochao/test/lnr.txt', 'r') as f:
        ehrids = f.readlines()
        ehrids = [x.strip() for x in ehrids]
        print(ehrids)


def send_request():
    # 启奥系统 - 人员列表
    # POST http://jkda.xamwjw.gov.cn/orguser/queryUserByParams.action

    try:
        response = requests.post(
            url="http://jkda.xamwjw.gov.cn/orguser/queryUserByParams.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Cookie": "JSESSIONID=4EFDB50B89669BC2ED010CF8461C43E3.tomcatA1; Shinow=suliyun; shinow_is_max=0",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "orgUserBean.sex": "",
                "page": "1",
                "orgUserBean.orgperStatus": "",
                "start": "0",
                "orgUserBean.technicTitle": "",
                "orgUserBean.positionCode": "",
                "limit": "10000",
                "jsonResult": "true",
                "orgUserBean.empName": "",
                "orgUserBean.idNo": "",
                "orgUserBean.deptId": "",
            },
        )
        result = response.json()

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


if __name__ == '__main__':
    diff_lnr()
