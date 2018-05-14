#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/11
import pymysql
from pipenv.utils import requests

from qiao_2_ksc import MYSQL_CONF_LOCAL, MYSQL_CONF_DEV, login


def get_organization(session):
    # 启奥系统 - 机构
    # POST http://jkda.xamwjw.gov.cn/org/queryOrganizationTreeForOrgList.action

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/org/queryOrganizationTreeForOrgList.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "orgInfo.orgStatus": "",
                "node": "root",
                "orgInfo.orgCode": "",
                "jsonResult": "true",
                "orgInfo.createPeople": "",
                "orgInfo.orgName": "",
                "orgInfo.orgType": "",
            },
        )
        return response.json()

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def main():
    # mysql
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    # get
    session = login('xingjinhua', '123456789')
    r = get_organization(session)
    children = r['children'][0]['children'][0]['children']
    type_map = {
        "盟/市卫生局": '1',
        "区/县卫生局": '2',
        "卫生服务中心/卫生院": '4',
        "卫生服务站/卫生室": '5',
    }
    sql = 'INSERT INTO sjzq_jg (bm,mc,sjbm,state,lx,prj) VALUES (%s,%s,%s,%s,%s,%s)'
    for i in children:
        SJBM = '152222000'
        BM = i['orgCode']
        MC = i['orgName']
        LX = type_map[i['orgType']]
        children = i['children']
        cursor.execute(sql, (BM, MC, SJBM, '1', LX, '1'))
        if children:
            for ii in children:
                SJBM = BM
                BM = ii['orgCode']
                MC = ii['orgName']
                LX = type_map[ii['orgType']]
                cursor.execute(sql, (BM, MC, SJBM, '1', LX, '1'))
    connect.commit()
    connect.close()


if __name__ == '__main__':
    main()
