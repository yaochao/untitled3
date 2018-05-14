#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/11
import pymysql
from pipenv.utils import requests
from qiao_2_ksc import MYSQL_CONF_LOCAL, MYSQL_CONF_DEV, login, user_pass_list


def get_department(session):
    # 启奥系统 - 科室
    # POST http://jkda.xamwjw.gov.cn/dept/queryDeptByParams.action

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/dept/queryDeptByParams.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "dept.deptName": "",
                "start": "0",
                "dept.deptType": "",
                "limit": "10000",
                "jsonResult": "true￼Name",
                "page": "1",
                "dept.deptCode": "",
            },
        )
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def main():
    # mysql
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    cursor2 = connect.cursor()
    # get
    for i in user_pass_list:
        name = i[0]
        print('正在抓取: {}'.format(name))
        username = i[1]
        password = i[2]
        session = login(username, password)
        result = get_department(session=session)
        sql = 'INSERT INTO sjzq_ks (sqbm,bm,mc,state,prj) VALUES (%s,%s,%s,%s,%s)'
        for i in result['pageResult']['pages']:
            ORG_NAME = i['ORG_NAME']
            sql2 = 'SELECT BM FROM sjzq_jg WHERE MC=%s'
            cursor2.execute(sql2, (ORG_NAME))
            result = cursor2.fetchone()
            BM = result['BM']
            DEPT_ID = i['DEPT_ID']
            DEPT_NAME = i['DEPT_NAME']
            state = 1
            prj = 1
            cursor.execute(sql, (BM, DEPT_ID, DEPT_NAME, state, prj))
    connect.commit()
    connect.close()

if __name__ == '__main__':
    main()
