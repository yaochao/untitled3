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


'''
[{
		"PROFESS_CODE": "11",
		"VAL": "执业医师",
		"PROFESS_NAME": "执业医师",
		"KEY": "11"
	}, {
		"PROFESS_CODE": "12",
		"VAL": "执业助理医师",
		"PROFESS_NAME": "执业助理医师",
		"KEY": "12"
	}, {
		"PROFESS_CODE": "13",
		"VAL": "见习医师",
		"PROFESS_NAME": "见习医师",
		"KEY": "13"
	}, {
		"PROFESS_CODE": "21",
		"VAL": "注册护士",
		"PROFESS_NAME": "注册护士",
		"KEY": "21"
	}, {
		"PROFESS_CODE": "22",
		"VAL": "助产士",
		"PROFESS_NAME": "助产士",
		"KEY": "22"
	}, {
		"PROFESS_CODE": "31",
		"VAL": "西药师(士)",
		"PROFESS_NAME": "西药师(士)",
		"KEY": "31"
	}, {
		"PROFESS_CODE": "32",
		"VAL": "中药师(士)",
		"PROFESS_NAME": "中药师(士)",
		"KEY": "32"
	}, {
		"PROFESS_CODE": "41",
		"VAL": "检验技师(士)",
		"PROFESS_NAME": "检验技师(士)",
		"KEY": "41"
	}, {
		"PROFESS_CODE": "42",
		"VAL": "影像技师(士)",
		"PROFESS_NAME": "影像技师(士)",
		"KEY": "42"
	}, {
		"PROFESS_CODE": "50",
		"VAL": "卫生监督员",
		"PROFESS_NAME": "卫生监督员",
		"KEY": "50"
	}, {
		"PROFESS_CODE": "69",
		"VAL": "其他卫生技术人员",
		"PROFESS_NAME": "其他卫生技术人员",
		"KEY": "69"
	}, {
		"PROFESS_CODE": "70",
		"VAL": "其他技术人员",
		"PROFESS_NAME": "其他技术人员",
		"KEY": "70"
	}, {
		"PROFESS_CODE": "80",
		"VAL": "管理人员",
		"PROFESS_NAME": "管理人员",
		"KEY": "80"
	}, {
		"PROFESS_CODE": "90",
		"VAL": "工勤及技能人员",
		"PROFESS_NAME": "工勤及技能人员",
		"KEY": "90"
	}],
'''
lb_map = {
    # TODO 医生类别映射

    '11': '2',
    '12': '2',
    '13': '2',
    '21': '4',
    '22': '3',
    '31': '2',
    '32': '2',
    '41': '2',
    '42': '2',
    '50': '8',
    '69': '8',
    '70': '8',
    '80': '5',
    '90': '8',
}


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
