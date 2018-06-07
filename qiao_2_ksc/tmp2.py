#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/21
import pymongo
import requests
import pymysql
from pymongo.errors import DuplicateKeyError

MONGO_CONF2 = {
    'host': '127.0.0.1',
    'port': 27018,
}

MONGO_CONF = {
    'host': '127.0.0.1',
    'port': 27017,
}

MYSQL_CONF_DEV = {
    'host': '127.0.0.1',
    'port': 8891,
    'user': 'phstest',
    'passwd': 'phstest@20161205',
    'db': 'g_lb',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

# mysql init
connect = pymysql.connect(**MYSQL_CONF_DEV)

# mongodb init
client = pymongo.MongoClient(**MONGO_CONF2)
client2 = pymongo.MongoClient(**MONGO_CONF2)
db2 = client2['datasets']
xam_person_detail_514 = db2['xam_person_detail_514']

db = client['datasets']
xam_et_list_521 = db['xam_et_list_521']
xam_ycf_list_521 = db['xam_jsb_list_521']
xam_lnr_list_522 = db['xam_lnr_list_522']
xam_fjh_list_521 = db['xam_fjh_list_521']
xam_tnb_list_521 = db['xam_tnb_list_521']
xam_gxy_list_521 = db['xam_gxy_list_521']


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


def get_et_list(session):
    # 启奥系统 - 儿童列表

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/grid/page/query.action",
            params={
                "gridCode": "ph_cld_grid",
                "paging": "1",
                "_dc": "1526902971795",
            },
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
                "Accept-Language": "zh_CN",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "start": "0",
                "parameter.ehrid": "",
                "parameter.fmTel": "",
                "jsonResult": "true",
                "parameter.p_name": "",
                "parameter.dsn": "",
                "parameter.filetype": "",
                "parameter.fmName": "",
                "parameter.R_org": "001001002",
                "limit": "1000000",
                "page": "1",
                "parameter.id_no": "",
            },
        )
        result = response.json()
        print('儿童total:%s' % result['resultData']['totalProperty'])
        for i in result['resultData']['pageData']:
            ehrId = i['EHR_ID']
            i['_id'] = ehrId
            try:
                xam_et_list_521.insert(i)
            except DuplicateKeyError as e:
                print(e)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_ycf_list(session):
    # 启奥系统 - 孕产妇列表

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/grid/page/query.action",
            params={
                "gridCode": "ph_pm_grid",
                "paging": "1",
                "_dc": "1526904782437",
            },
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
                "Cookie": "JSESSIONID=32A77C27BF593F9E259AF16C40B01DA3.tomcatA1; Shinow=xingjinhua; shinow_is_max=0",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
                "Accept-Language": "zh_CN",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "parameter.enddate": "",
                "parameter.ehrid": "",
                "start": "0",
                "jsonResult": "true",
                "parameter.p_name": "",
                "parameter.org": "001001002",
                "parameter.dsn": "",
                "parameter.jieduan": "",
                "parameter.startdate": "",
                "parameter.filetype": "",
                "limit": "1000000",
                "page": "1",
                "parameter.id_no": "",
            },
        )
        result = response.json()
        print('孕产妇total:%s' % result['resultData']['totalProperty'])
        for i in result['resultData']['pageData']:
            ehrId = i['EHR_ID']
            i['_id'] = ehrId
            try:
                xam_ycf_list_521.insert(i)
            except DuplicateKeyError as e:
                print(e)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_lnr_list():
    # 启奥系统 - 老年人列表

    try:
        response = requests.post(
            url="http://jkda.xamwjw.gov.cn/grid/page/query.action",
            params={
                "gridCode": "ph_op_grid",
                "paging": "1",
                "_dc": "1526975244060",
            },
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
                "Cookie": "JSESSIONID=FA6DA32EE0ED53F8EB16AFD6404A6A42.tomcatA1; Shinow=xingjinhua; shinow_is_max=0",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
                "Accept-Language": "zh_CN",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "parameter.ehrstatus": "0",
                "parameter.ehrid": "",
                "start": "0",
                "parameter.year_service": "0",
                "parameter.p_name": "",
                "parameter.year": "2018",
                "parameter.org": "001001002",
                "parameter.start_date": "",
                "parameter.end_date": "",
                "parameter.dsn": "",
                "parameter.filetype": "0",
                "jsonResult": "true",
                "limit": "1000000",
                "page": "1",
                "parameter.id_no": "",
            },
        )
        result = response.json()
        print('老年人total:%s' % result['resultData']['totalProperty'])
        for i in result['resultData']['pageData']:
            ehrId = i['EHR_ID']
            i['_id'] = ehrId
            print(ehrId)
            try:
                xam_lnr_list_522.insert(i)
            except DuplicateKeyError as e:
                print(e)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_gxy_list(session):
    # 启奥系统 - 高血压列表

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/grid/page/query.action",
            params={
                "gridCode": "ph_hyp_grid",
                "paging": "1",
                "_dc": "1526905119186",
            },
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
                "Accept-Language": "zh_CN",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "start": "0",
                "parameter.ehrid": "",
                "jsonResult": "true",
                "parameter.year_service": "0",
                "parameter.p_name": "",
                "parameter.year": "2018",
                "parameter.start_date": "",
                "parameter.end_date": "",
                "parameter.dsn": "",
                "parameter.filetype": "0",
                "parameter.R_org": "001001002",
                "parameter.age": "35",
                "limit": "1000000",
                "page": "1",
                "parameter.id_no": "",
            },
        )
        result = response.json()
        print('高血压total:%s' % result['resultData']['totalProperty'])
        for i in result['resultData']['pageData']:
            ehrId = i['EHR_ID']
            i['_id'] = ehrId
            try:
                xam_gxy_list_521.insert(i)
            except DuplicateKeyError as e:
                print(e)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def fix_et():
    cursor = connect.cursor()
    cursor2 = xam_et_list_521.find()
    sql = 'SELECT iset FROM sjzq_grda where bm=%s'
    sql2 = 'UPDATE sjzq_grda SET iset=1,isupdate=-4 where bm=%s'
    for i in cursor2:
        ehrId = i['_id']
        cursor.execute(sql, (ehrId))
        result = cursor.fetchone()
        if result and result['iset'] == 0:
            cursor.execute(sql2, (ehrId))
            connect.commit()


def fix_gxy():
    cursor = connect.cursor()
    sql = 'SELECT bm FROM sjzq_grda where isgxy=1'
    sql2 = 'UPDATE sjzq_grda SET isgxy=0,isupdate=-3 where bm=%s'
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        bm = i['bm']
        r = xam_gxy_list_521.find({'_id': bm}).count()
        if not r:
            cursor.execute(sql2, bm)
            connect.commit()
            print(r)


def fix_tnb():
    cursor = connect.cursor()
    cursor2 = xam_tnb_list_521.find()
    sql = 'SELECT bm FROM sjzq_grda where istnb=1'
    sql2 = 'UPDATE sjzq_grda SET istnb=0,isupdate=-5 where bm=%s'
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        bm = i['bm']
        r = xam_tnb_list_521.find({'_id': bm}).count()
        if not r:
            print(r)


def fix_lnr():
    cursor = connect.cursor()
    cursor2 = xam_lnr_list_522.find()
    sql = 'SELECT islnr FROM sjzq_grda where bm=%s'
    sql2 = 'UPDATE sjzq_grda SET islnr=1,isupdate=-6 where bm=%s'
    for i in cursor2:
        ehrId = i['_id']
        cursor.execute(sql, (ehrId))
        result = cursor.fetchone()
        if result and result['islnr'] == 0:
            print(ehrId)
            cursor.execute(sql2, (ehrId))
            connect.commit()


def diff_lnr():
    cursor = connect.cursor()
    sql = 'SELECT DISTINCT bm FROM sjzq_grda WHERE isupdate=-6;'
    sql2 = 'SELECT bm FROM sjzq_grda WHERE isupdate=-6;'
    cursor.execute(sql)
    result = cursor.fetchall()
    result = [x['bm'] for x in result]
    print(len(result))

    cursor.execute(sql2)
    result2 = cursor.fetchall()
    result2 = [x['bm'] for x in result2]
    print(len(result2))
    for i in result:
        result2.remove(i)
    print(result2)


def diff_lnr2():
    with open('522已插入的老年人.txt') as f:
        result = f.readlines()
        result = [x.split('\t')[0] for x in result]
    with open('老年人档案更新.txt') as f:
        result2 = f.readlines()
        result2 = [x.split('bm=\'')[-1].split('\'')[0] for x in result2]
    not_insert = []
    for i in result2:
        if i not in result:
            not_insert.append(i)
    print(len(not_insert))
    with open('522未插入的老年人bm.txt', 'w') as f:
        f.write('\n'.join(not_insert))


def diff_hjdz_xzz_code():
    cursor = xam_person_detail_514.find({}, {'person.addrcodePresent': 1, 'person.ehrId': 1})
    diff_ehrIds = []
    diff_ehrIds2 = []
    sql = '''
UPDATE da_dz a join da_grda0 b on a.dzfk=b.empi SET a.DZ3='{}', a.DZ4='{}',a.DZ5='{}' WHERE b.DAH ='{}';
UPDATE da_grda1 a join da_grda0 b on a.EMPI=b.empi SET a.JTDZ3='{}', a.JTDZ4='{}',a.JTDZ5='{}' WHERE b.DAH ='{}';
UPDATE person_info a join da_grda0 b on a.EMPI=b.empi SET a.JTDZ3='{}',a.JTDZ4='{}',a.JTDZ5='{}' WHERE b.DAH ='{}';
'''
    for i in cursor:
        addrcodePresent = i['person']['addrcodePresent']
        ehrId = i['person']['ehrId']
        if addrcodePresent:
            if addrcodePresent != ehrId[:12]:
                try:
                    addrcodePresent = int(addrcodePresent)
                    addrcodePresent = str(addrcodePresent)
                    DZ3 = addrcodePresent[:6]
                    DZ4 = addrcodePresent[:9]
                    DZ5 = addrcodePresent[:12]
                    diff_ehrIds.append(sql.format(DZ3, DZ4, DZ5, ehrId, DZ3, DZ4, DZ5, ehrId, DZ3, DZ4, DZ5, ehrId))
                except:
                    diff_ehrIds2.append(ehrId + ' ' + str(addrcodePresent) + '\n')
    print(len(diff_ehrIds) / 3)
    print(len(diff_ehrIds2))
    with open('diff_hjdz_xzz.txt', 'w') as f:
        f.writelines(diff_ehrIds)

    with open('diff_hjdz_xzz2.txt', 'w') as f:
        f.writelines(diff_ehrIds2)


def main():
    session = login('xingjinhua', '123456789')
    get_gxy_list(session)


if __name__ == '__main__':
    diff_hjdz_xzz_code()
