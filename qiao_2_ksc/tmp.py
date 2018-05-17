#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/15


from qiao_2_ksc import MYSQL_CONF_DEV, MYSQL_CONF_LOCAL
import pymysql

connect = pymysql.connect(**MYSQL_CONF_DEV)
cursor = connect.cursor()
cursor2 = connect.cursor()

def update_sjzq_ry():
    sql = 'SELECT * FROM sjzq_ry'
    cursor.execute(sql)
    result = cursor.fetchall()
    for index, i in enumerate(result):
        print(i)
        # sql = 'UPDATE sjzq_grda SET zrysid=%s WHERE sqbm=%s AND zrys=%s AND zrysid is null'
        sql = 'UPDATE sjzq_grda SET jdryid=%s,jdry=%s WHERE sqbm=%s AND jdrymc=%s AND jdryid is null'
        cursor.execute(sql, (i['bm'], i['bm'], i['sqbm'], i['mc']))
        connect.commit()
    connect.close()


def create_ry():
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
        bm = sqbm + 'B'+str(index)
        state = 1
        prj = 1
        print(index)
        sql = 'INSERT INTO sjzq_ry (sqbm, bm, mc, state, prj) values (%s,%s,%s,%s,%s)'
        cursor.execute(sql, (sqbm, bm, zrys, state, prj))
    connect.commit()
    connect.close()


def change_sqbm_add_1522():

    # select sqbm start with '22'
    sql = 'SELECT DISTINCT sqbm FROM sjzq_grda WHERE sqbm LIKE "22%"'
    cursor.execute(sql)
    result = cursor.fetchall()
    result = [i['sqbm'] for i in result]

    #update
    sql2 = 'UPDATE sjzq_grda SET sqbm=%s WHERE sqbm=%s'
    for i in result:
        print(i)
        new_sqbm = '1522' + i
        cursor.execute(sql2, (new_sqbm, i))
        connect.commit()
    connect.close()





if __name__ == '__main__':
    change_sqbm_add_1522()