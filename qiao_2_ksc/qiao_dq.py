#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/10
import requests
from pprint import pprint
import pymysql
from qiao_2_ksc import login, MYSQL_CONF_LOCAL, MYSQL_CONF_DEV




def get_region_code(session, region_code="152222"):

    try:
        response = session.get(
            url="http://jkda.xamwjw.gov.cn/ph/queryDsnTree.action",
            params={
                "_dc": "1525946535905",
                "id": region_code,
                "jsonResult": "true",
            },
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "Host": "jkda.xamwjw.gov.cn",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "http://jkda.xamwjw.gov.cn/loadTpl.action?tplId=Hr_pi&tplScript=hr,IdCardNoCheck",
            },
        )
        dsnTreeList = response.json()['dsnTreeList']
        return dsnTreeList
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def main():
    # Mysql
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    # 兴安盟县下面的镇列表
    session = login('xingjinhua', '123456789')
    dsnTreeList = get_region_code(session=session, region_code='152222')
    print(dsnTreeList)
    sql = 'INSERT INTO sjzq_dq (bm,mc,sjbm,lx,prj) VALUES (%s, %s, %s, %s, %s)'
    for i in dsnTreeList:
        town_id = i['id']
        town_text = i['text']
        cursor.execute(sql, (town_id, town_text, '152222', '5', '1'))
        dsnTreeList2 = get_region_code(session=session, region_code=town_id)
        for ii in dsnTreeList2:
            village_id = ii['id']
            village_text = ii['text']
            cursor.execute(sql, (village_id, village_text, town_id, '5', '1'))
        connect.commit()
    connect.close()


if __name__ == '__main__':
    main()