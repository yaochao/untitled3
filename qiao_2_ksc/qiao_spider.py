#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/4

import requests
import random
import pymongo
from pymongo.errors import DuplicateKeyError
from qiao_2_ksc import login

MONGO_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
}
client = pymongo.MongoClient(**MONGO_CONFIG)
db = client['datasets']
collection_list_514 = db['xam_person_list_514']
collection_list_417 = db['xam_person_list']
collection_detail = db['xam_person_detail_514']
collection_error = db['xam_error_514']


def get_cookie():
    session_ids = ['C8CB4AC1B4622569FCE61A828B0EB74B.tomcatA1']
    cookie = 'Shinow=xingjinhua; shinow_is_max=0; JSESSIONID={sessionid}'.format(sessionid=random.choice(session_ids))
    return cookie


def get_list(session):
    # 个人档案列表

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/grid/page/query.action",
            params={
                "gridCode": "ph_hr_grid",
                "paging": "1",
            },
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
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
                "limit": "{limit}".format(limit=208485),
                "parameter.dsn": "",
            },
        )
        page_data = response.json()['resultData']['pageData']
        print(len(page_data))
        for i in page_data:
            i['_id'] = i['SERIAL_CODE']
            collection_list_514.insert(i)
        return page_data
    except Exception as e:
        print('HTTP Request failed: {}'.format(e))


def get_detail(serial_code, session):
    # 个人档案详细信息
    # POST http://jkda.xamwjw.gov.cn/ph/queryHr.action
    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/ph/queryHr.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
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
                "peId": "{}".format(serial_code),
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
    for i in range(208, 209):
        print('now:', str([i * 1000, (i + 1) * 1000]))
        cursor = collection_list_514.find({}, {"_id": 1}).skip((i * 1000)).limit(1000)
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

def re_get_error_detail():
    cursor = collection_detail.find({"sessionInvalid": "本次会话已过期,请重新登录！！"}, {"_id": 1})
    result = list(cursor)
    print(len(result))
    for i in result:
        serial_code = i['_id']
        # 1. 先删除,再重新下载，插入mongo
        collection_detail.remove({"_id": serial_code})

        try:
            pe_id = serial_code
            person_ehr = get_detail(serial_code, pe_id)
            if not person_ehr:
                continue
            if 'sessionInvalid' in person_ehr.keys():
                print(person_ehr['sessionInvalid'])
                break
            person_ehr['_id'] = serial_code
            print(serial_code, ' - ', person_ehr['person']['pName'])
            # 2. 插入mongo
            collection_detail.insert(person_ehr)
        except Exception as e:
            print(e)


def get_diff_list_detail():
    cursor = collection_list_514.find({}, {'_id': 1})
    result = list(cursor)
    list_ids = [i['_id'] for i in result]

    cursor2 = collection_detail.find({}, {'_id': 1})
    result2 = list(cursor2)
    detail_ids = [i['_id'] for i in result2]

    for i in list_ids:
        if i in detail_ids[:-1]:
            detail_ids.remove(i)
        else:
            try:
                serial_code = i
                pe_id = serial_code
                person_ehr = get_detail(serial_code, pe_id)
                if not person_ehr:
                    continue
                if 'sessionInvalid' in person_ehr.keys():
                    print(person_ehr['sessionInvalid'])
                    break
                person_ehr['_id'] = serial_code
                print(serial_code, ' - ', person_ehr['person']['pName'])
                # 2. 插入mongo
                collection_detail.insert(person_ehr)
            except Exception as e:
                print(e)


def get_diff_list_detail2():
    # listid:1679238 对应的detailid:1929114
    # listid:1165998 对应的detailid:1929081
    # listid:546203 对应的detailid:1929306
    # listid:402000 对应的detailid:1929275
    # listid:343894 对应的detailid:1929168
    ids = ['1929306', '1929275', '1929168']

    for i in ids:
        try:
            serial_code = i
            pe_id = serial_code
            person_ehr = get_detail(serial_code, pe_id)
            if not person_ehr:
                continue
            if 'sessionInvalid' in person_ehr.keys():
                print(person_ehr['sessionInvalid'])
                break
            person_ehr['_id'] = serial_code
            print(serial_code, ' - ', person_ehr['person']['pName'])
            collection_detail.insert(person_ehr)
        except Exception as e:
            print(e)


def data_verify():
    '''
    数据完整性校验
    :return:
    '''
    cursor = collection_list_514.find({}, {"_id": 1, "P_NAME": 1})
    result = list(cursor)
    for i in result:
        _id = i['_id']
        P_NAME = i['P_NAME']
        cursor2 = collection_detail.find({"_id": _id}, {"person": 1})
        result2 = list(cursor2)
        if result2:
            if result2[0]['person']['pName'] == P_NAME:
                continue
            print('list:', P_NAME, 'detail:', result2[0]['person']['pName'], _id)
        else:
            print('detail中找不到id:', _id)
    # 结果, 总结：姓名基本都是空格导致，有一个是输入错误。
    # 找不到的5条，已经全部在detail，原因是list和detail的SERIAL_ID对应不上。
    # '''
    # list:  出伦巴根 detail: 出伦巴根 1924911
    # list: 阿斯瀚  detail: 阿斯瀚 1913487
    # list:   关嘉琪 detail: 关嘉琪 1879116
    # list: 	玉晓 detail: 玉晓 1871845
    # list: 赵红全	 detail: 赵红全 1871838
    # detail中找不到id: 1679238
    # list:  包世杰 detail: 包世杰 1193433
    # list:  代伟 detail: 代伟 1191603
    # detail中找不到id: 1165998
    # detail中找不到id: 546203
    # list: 叶宝小  detail: 叶宝小 540352
    # detail中找不到id: 402000
    # list: 韩金花 detail: 韩金虎 395496
    # detail中找不到id: 343894
    # '''


def get_diff_417_514():
    cursor_417 = collection_list_417.find({}, {'_id': 1})
    cursor_514 = collection_list_514.find({}, {'_id': 1})
    _id_all_417 = []
    _id_all_514 = []
    for i in cursor_417:
        _id_all_417.append(i['_id'])
    print('417 total:', len(_id_all_417))
    for i in cursor_514:
        _id_all_514.append(i['_id'])
    print('514 total:', len(_id_all_514))
    # 比较两个数组的不同:
    ## 514不在417的id
    not_in_417 = []
    for i in _id_all_514:
        if i not in _id_all_417:
            not_in_417.append(i)
    print('not in 417 total:', len(not_in_417))
    # 保存下来
    with open('not_in_417.txt', 'w') as f:
        f.write('\n'.join(not_in_417))

    ## 417不在514的id
    not_in_514 = []
    for i in _id_all_417:
        if i not in _id_all_514:
            not_in_514.append(i)
    print('not in 514 total:', len(not_in_514))
    # 保存下来
    with open('not_in_514.txt', 'w') as f:
        f.write('\n'.join(not_in_514))


def get_detail_514():
    # 把514中比417多的ID加入
    # login
    session = login('xingjinhua', '123456789')
    # get id form txt
    with open('not_in_417.txt', 'r') as f:
        result = f.readlines()
        result = [x.strip() for x in result]
    # get detail with id and session, and insert into mongodb.
    while True:
        try:
            serial_code = result.pop()
        except IndexError as e:
            print('completed:', e)
            break
        try:
            person_ehr = get_detail(serial_code, session)
            if not person_ehr:
                print('serial_code {} got None result'.format(serial_code))
                continue
            if 'sessionInvalid' in person_ehr.keys():
                print(person_ehr['sessionInvalid'])
                session = login('xingjinhua', '123456789')
                result.append(serial_code)
            person_ehr['_id'] = serial_code
            print(serial_code, ' - ', person_ehr['person']['pName'])
            collection_detail.insert(person_ehr)
        except Exception as e:
            print(e)


def remove_detail_417():
    # 把417中比514中多的ID去掉
    with open('not_in_514.txt', 'r') as f:
        result = f.readlines()
        result = [x.strip() for x in result]
        print(result)
    for serial_code in result:
        try:
            collection_detail.remove({'_id': serial_code})
        except Exception as e:
            print(e)


if __name__ == '__main__':
    data_verify()