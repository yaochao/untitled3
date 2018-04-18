#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/4

import requests
import random
import pymongo
from pymongo.errors import DuplicateKeyError

MONGO_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
}
client = pymongo.MongoClient(**MONGO_CONFIG)
db = client['datasets']
collection_list = db['xam_person_list']
collection_detail = db['xam_person_detail']
collection_error = db['xam_error']


def get_cookie():
    session_ids = ['D236097C8128FADD8B3266BC1501F529.tomcatA1', '20DABB5471423719ECE8C55961EDC7C3.tomcatA1', '473BD21F51A8EF3893FB5098AA316382.tomcatA1', 'F5FE5C484244F8343197A7E29B97862A.tomcatA1']
    cookie = 'Shinow=xingjinhua; shinow_is_max=0; JSESSIONID={sessionid}'.format(sessionid=random.choice(session_ids))
    return cookie


def get_list():
    # 个人档案列表

    try:
        response = requests.post(
            url="http://jkda.xamwjw.gov.cn/grid/page/query.action",
            params={
                "gridCode": "ph_hr_grid",
                "paging": "1",
            },
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
                "Cookie": get_cookie(),
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                "Accept-Language": "zh_CN",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "parameter.id_no": "",
                "parameter.doctor": "",
                "parameter.ehrid": "",
                "parameter.startCreateDate": "",
                "parameter.complete": "",
                "parameter.addr": "",
                "parameter.p_name": "",
                "parameter.enddate": "",
                "parameter.filetype": "0",
                "parameter.R_addrRegi": "",
                "parameter.startdate": "",
                "parameter.startage": "",
                "parameter.sex": "",
                "parameter.ehrstatus": "0",
                "parameter.endCreateDate": "",
                "jsonResult": "true",
                "parameter.org": "001001002",
                "parameter.endage": "",
                "page": "{page}".format(page=1),
                "start": "{start}".format(start=0),
                "limit": "{limit}".format(limit=208339),
                "parameter.dsn": "",
            },
        )
        page_data = response.json()['resultData']['pageData']
        print(len(page_data))
        for i in page_data:
            i['_id'] = i['SERIAL_CODE']
            collection_list.insert(i)
        return page_data
    except Exception as e:
        print('HTTP Request failed: {}'.format(e))


def get_detail(serial_code, pe_id):
    # 个人档案详细信息
    # POST http://jkda.xamwjw.gov.cn/ph/queryHr.action
    try:
        response = requests.post(
            url="http://jkda.xamwjw.gov.cn/ph/queryHr.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
                "Cookie": get_cookie(),
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                "Accept-Language": "zh_CN",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "jsonResult": "true￼Name",
                "serialCode": "{}".format(serial_code),
                "peId": "{}".format(pe_id),
            },
        )
        person_ehr = response.json()
        return person_ehr
    except Exception as e:
        print('{}, {}'.format(e, serial_code))
        collection_error.insert({
            '_id': serial_code,
            'error': str(e),
            'function': 'get_detail'
        })


def get_all_detail():
    for i in range(100, 140):
        print('now:', str([i * 1000, (i + 1) * 1000]))
        cursor = collection_list.find({}, {"_id": 1}).skip((i * 1000)).limit(1000)
        result = list(cursor)
        for ii in result:
            serial_code = ii['_id']
            try:
                pe_id = serial_code
                person_ehr = get_detail(serial_code, pe_id)
                if not person_ehr:
                    continue
                person_ehr['_id'] = serial_code
                print(serial_code, ' - ', person_ehr['person']['pName'])
                collection_detail.insert(person_ehr)
            except Exception as e:
                try:
                    collection_error.insert({
                        '_id': serial_code,
                        'error': str(e),
                        'function': 'get_all_detail'
                    })
                except DuplicateKeyError as e:
                    print(e)


if __name__ == '__main__':
    get_all_detail()
