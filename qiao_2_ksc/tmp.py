#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/15
import pymongo
import pymysql

MYSQL_CONF_LOCAL = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'toor',
    'db': 'work2',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
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

MYSQL_CONF_DEV2 = {
    'host': '172.31.48.2',
    'port': 8091,
    'user': 'phstest',
    'passwd': 'phstest@20161205',
    'db': 'g_lb',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

MONGO_CONF = {
    'host': '127.0.0.1',
    'port': 27017,
}

MONGO_CONF2 = {
    'host': '127.0.0.1',
    'port': 27018,
}


def update_sjzq_ry():
    '''
    把创建的人员更新到个人档案对应的建档人员和责任医生
    :return:
    '''
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    sql = 'SELECT * FROM sjzq_ry'
    cursor.execute(sql)
    result = cursor.fetchall()
    for index, i in enumerate(result):
        print(i)
        sql = 'UPDATE sjzq_grda SET zrysid=%s WHERE sqbm=%s AND zrys=%s AND zrysid is null'
        sql2 = 'UPDATE sjzq_grda SET jdryid=%s,jdry=%s WHERE sqbm=%s AND jdrymc=%s AND jdryid is null'
        cursor.execute(sql, (i['bm'], i['sqbm'], i['mc']))
        connect.commit()
        cursor.execute(sql2, (i['bm'], i['bm'], i['sqbm'], i['mc']))
        connect.commit()
    connect.close()


def create_ry():
    '''
    创建人员
    :return:
    '''
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    # sql = 'SELECT sqbm, zrys FROM sjzq_grda where zrysid is null and zrys is not null'
    sql = 'SELECT sqbm, jdrymc FROM sjzq_grda where jdryid is null and jdrymc is not null'
    cursor.execute(sql)
    result = cursor.fetchall()
    all_set = set()
    for i in result:
        sqbm = i['sqbm']
        zrys = i['jdrymc']
        all_set.add((sqbm, zrys))
    print('total: ', len(all_set))
    for index, i in enumerate(all_set):
        sqbm = i[0]
        zrys = i[1]
        bm = sqbm + 'B' + str(index)
        state = 1
        prj = 1
        print(index)
        sql = 'INSERT INTO sjzq_ry (sqbm, bm, mc, state, prj) values (%s,%s,%s,%s,%s)'
        cursor.execute(sql, (sqbm, bm, zrys, state, prj))
    connect.commit()
    connect.close()


def change_sqbm_add_1522():
    '''
    把个人档案里面机构的编码，开头为22的，加上1522.
    :return:
    '''
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    # select sqbm start with '22'
    sql = 'SELECT DISTINCT sqbm FROM sjzq_grda WHERE sqbm LIKE "22%"'
    cursor.execute(sql)
    result = cursor.fetchallm()
    result = [i['sqbm'] for i in result]

    # update
    sql2 = 'UPDATE sjzq_grda SET sqbm=%s WHERE sqbm=%s'
    for i in result:
        print(i)
        new_sqbm = '1522' + i
        cursor.execute(sql2, (new_sqbm, i))
        connect.commit()
    connect.close()


def fix_fjh():
    '''
    错误原因：本该为0的肺结核，弄错为1了，找出这些弄错的，并把isupdate改为-2
    :return:
    '''
    # mysql
    connect = pymysql.connect(**MYSQL_CONF_DEV)
    cursor = connect.cursor()
    # mongo
    client = pymongo.MongoClient(**MONGO_CONF2)
    db = client['datasets']
    collection = db['xam_person_list_518']
    result = collection.find({"FEA_PTB": {"$eq": 0}})
    for i in result:
        ehrId = i['EHR_ID']
        sql = 'UPDATE sjzq_grda SET isupdate=-2,isfjh=0 where bm=%s and isfjh=1'
        cursor.execute(sql, (ehrId))
        print(ehrId)
        connect.commit()
    connect.close()


if __name__ == '__main__':
    fix_fjh()
