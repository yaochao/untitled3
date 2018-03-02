#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/1


import requests
import pymysql

query_list_url_gc = 'http://appcfda.drugwebcn.com/datasearch/QueryList?tableId=25&pageIndex=10&pageSize=165854' # 国产list 165854
query_list_url_jk = 'http://appcfda.drugwebcn.com/datasearch/QueryList?tableId=36&pageIndex=1&pageSize=4089' # 进口list 4089
query_list_url_jb = 'http://appcfda.drugwebcn.com/datasearch/QueryList?tableId=74&pageIndex=1&pageSize=520' # 基本list 520
query_record_url_gc = 'http://appcfda.drugwebcn.com/datasearch/QueryRecord?tableId=25&searchF=ID&searchK=' # 国产详情
query_record_url_jk = 'http://appcfda.drugwebcn.com/datasearch/QueryRecord?tableId=36&searchF=ID&searchK=' # 进口详情
query_record_url_jb = 'http://appcfda.drugwebcn.com/datasearch/QueryRecord?tableId=74&searchF=ID&searchK=' # 进口详情
mysql_conf = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'work',
    'charset': 'utf8',
}
conn = pymysql.Connect(**mysql_conf)
cursor = conn.cursor()


def get_list():
    response = requests.get(query_list_url_jb)
    assert response.status_code == 200
    response = response.json()
    print(len(response))
    for item in response:
        ID = item['ID']
        CONTENT = item['CONTENT']
        order = CONTENT.split('.')[0]
        CONTENT = CONTENT.split(order+'.')[-1]
        sql = 'INSERT INTO `SYJ_JBYP_LIST` (ID, CONTENT) VALUES (%s, %s)'
        cursor.execute(sql, (ID, CONTENT))
    conn.commit()


def get_detail_main():
    url = query_list_url_jb
    response = requests.get(url)
    assert response.status_code == 200
    response = response.json()
    print('当前列表的个数为:',len(response))
    for index, item in enumerate(response):
        ID = item['ID']
        get_detail(ID, index)

def get_detail(ID, index):
    url = query_record_url_jb + ID
    response = requests.get(url)
    print('当前抓取的药品详情index:',index)
    assert response.status_code == 200
    response = response.json()
    response = [x['CONTENT'] for x in response]
    response.insert(0, ID)
    response = response[:-1]
    assert len(response) == 11 # 14 OR 33
    sql = 'INSERT INTO `SYJ_GCYP_DETAIL` (ID,PZWH,CPMC,YWMC,SPM,JX,GG,SCDW,SCDZ,CPLB,PZRQ,YPZWH,YPBWM,YPBWMBZ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sql_jk = 'INSERT INTO `SYJ_JKYP_DETAIL` (ID,ZCZH,YZCZH,ZCZHBZ,FBZPZWH,GSMCZW,GSMCYW,DZZW,DZYW,GJDQZW,GJDQYW,CPMCZW,CPMCYW,SPMZW,SPMYW,JXZW,GGZW,BZGGZW,SCCSZW,SCCSYW,CSDZZW,CSDZYW,CSGJDQZW,CSGJDQYW,FZRQ,YXQJZR,FBZQYMC,FBZQYDZ,FBZWHPZRQ,FBZWHYXQJZR,CPLB,YPBWM,YPBWMBZ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sql_jb = 'INSERT INTO `SYJ_JBYP_DETAIL` (ID,YPFL,YJLB,EJLB,SJLB,PZMCYPMC,YWMC,JXGG,JXSM,SYFW,BZ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql_jb, tuple(response))
    conn.commit()





if __name__ == '__main__':
    get_list()
