#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/11


import pymysql
from pipenv.utils import requests
from qiao_2_ksc import MYSQL_CONF_LOCAL, MYSQL_CONF_DEV, login, user_pass_list


def get_doctor(session):
    '''
    获取人员列表
    :param session:
    :return:
    '''
    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/orguser/queryUserByParams.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
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
                "limit": "26",
                "jsonResult": "true",
                "orgUserBean.empName": "",
                "orgUserBean.idNo": "",
                "orgUserBean.deptId": "",
            },
        )
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_doctor_detail(session, EMPID):
    # 启奥系统 - 人员详情
    # POST http://jkda.xamwjw.gov.cn/orguser/queryEntity.action
    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/orguser/queryEntity.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "empId": EMPID,
                "jsonResult": "true",
            },
        )
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def main():
    # mysql
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    # for
    for i in user_pass_list:
        name = i[0]
        print('正在抓取: {}'.format(name))
        username = i[1]
        password = i[2]
        session = login(username, password)
        # get doctor list
        result = get_doctor(session=session)
        sql = 'INSERT INTO sjzq_ry (sqbm,bm,mc,xb,lb,ksbm,state,csrq,sfzh,lxdh,prj) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for i in result['pageResult']['pages']:
            EMPID = i['EMPID']
            # get doctor detail
            result = get_doctor_detail(session, EMPID)
            orgUserBean = result['orgUserBean']

            sqbm = result['orgCode']
            if sqbm.startswith('22'):
                sqbm = '1522' + sqbm
            bm = orgUserBean['empId']
            mc = orgUserBean['empName']
            xb = orgUserBean['sex'] if orgUserBean['sex'] else '0'
            lb = '1' if orgUserBean['perType'] else '2'
            ksbm = orgUserBean['deptId']
            state = '1'
            csrq = orgUserBean['birthDate']
            sfzh = orgUserBean['idNo']
            lxdh = orgUserBean['telNo']
            prj = '1'
            cursor.execute(sql, (sqbm, bm, mc, xb, lb, ksbm, state, csrq, sfzh, lxdh, prj))
        connect.commit()
    connect.close()


if __name__ == '__main__':
    main()
