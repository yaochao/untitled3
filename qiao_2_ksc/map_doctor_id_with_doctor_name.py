#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/7
import random

import requests
import pymongo
from qiao_2_ksc import login, LoginTimeoutException

MONGO_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
}
client = pymongo.MongoClient(**MONGO_CONFIG)
db = client['datasets']
collection_doctor_list = db['xam_doctor_list']
collection_detail = db['xam_person_detail']
collection_error = db['xam_error']


def get_session(username, password, relogin=False):
    '''
    获取一个 requests 的 session 对象，改对象已经登录过，cookie里面保留了登录之后的信息
    :return:
    '''
    session = None
    if not session:
        session = login(username, password)
    if relogin:
        session = login(username, password)
    return session


def get_online_doctor():
    '''
    通过当地医院账号，获取到对应的医生
    :return:
    '''
    try:
        response = requests.post(
            url="http://jkda.xamwjw.gov.cn/orguser/queryUserByParams.action",

            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
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
                "limit": "27",
                "jsonResult": "true",
                "orgUserBean.empName": "",
                "orgUserBean.idNo": "",
                "orgUserBean.deptId": "",
            },
        )

        result = response.json()
        if 'sessionInvalid' in result.keys():
            print(result, '会话过期')
            return '会话过期'
        pages = result['pageResult']['pages']
        totalCount = result['pageResult']['totalCount']
        assert len(pages) == totalCount
        all_online_doctor = []
        for i in pages:
            EMPID = i['EMPID']
            EMPNAME = i['EMPNAME']
            # all_online_doctor.append((EMPID, EMPNAME))
            all_online_doctor.append(EMPNAME)
        return all_online_doctor
    except Exception as e:
        print(e)


def get_local_doctor():
    '''
    获取到健康档案详细信息里面的简单人员和责任医生
    :return:
    '''
    cursor = collection_detail.find({"person.createUnitName": "好腰苏木中心卫生院"}, {'person': 1})
    result = list(cursor)
    all_local_doctor = set()
    for i in result:
        creator = i['person']['creator']
        creatorName = i['person']['creatorName']
        # all_local_doctor.add((creator, creatorName))
        all_local_doctor.add(creatorName)
    return all_local_doctor


def main():
    # 1. local doctor
    all_local_doctor = get_local_doctor()
    # 2. online doctor
    all_online_doctor = get_online_doctor()
    print(all_local_doctor, len(all_local_doctor))
    print('*' * 50)
    print(all_online_doctor, len(all_online_doctor))
    # 3.判断local doctor不在online doctor的数量
    not_in_online = []
    for i in all_local_doctor:
        if i not in all_online_doctor:
            not_in_online.append(i)
    print(not_in_online, len(not_in_online))


if __name__ == '__main__':
    get_online_doctor()
