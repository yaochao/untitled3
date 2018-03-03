#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/3/1


import requests
import pymysql
import time

mysql_conf = {
    'host': '47.93.232.8',
    'port': 3306,
    'user': 'root',
    'password': 'W$udzpgobz#4evVs',
    'db': 'yaochao',
    'charset': 'utf8',
}
conn = pymysql.Connect(**mysql_conf)
cursor = conn.cursor()

cursor.execute('SELECT count(*) FROM SYJ_GCYP_DETAIL;')
r = cursor.fetchall()
r = r[0][0]
print(r)

query_list_url_gc = 'http://appcfda.drugwebcn.com/datasearch/QueryList?tableId=25&pageIndex=2&pageSize=' + str(r) # 国产list
query_list_url_jk = 'http://appcfda.drugwebcn.com/datasearch/QueryList?tableId=36&pageIndex=1&pageSize=4089' # 进口list
query_record_url_gc = 'http://appcfda.drugwebcn.com/datasearch/QueryRecord?tableId=25&searchF=ID&searchK=' # 国产详情
query_record_url_jk = 'http://appcfda.drugwebcn.com/datasearch/QueryRecord?tableId=36&searchF=ID&searchK=' # 进口详情
mysql_conf = {
    'host': '47.93.232.8',
    'port': 3306,
    'user': 'root',
    'password': 'W$udzpgobz#4evVs',
    'db': 'yaochao',
    'charset': 'utf8',
}



def get_list():
    response = requests.get(query_list_url_jk)
    assert response.status_code == 200
    response = response.json()
    print(len(response))
    for item in response:
        ID = item['ID']
        CONTENT = item['CONTENT']
        order = CONTENT.split('.')[0]
        CONTENT = CONTENT.split(order+'.')[-1]
        sql = 'INSERT INTO `SYJ_JKYP_LIST` (ID, CONTENT) VALUES (%s, %s)'
        cursor.execute(sql, (ID, CONTENT))
    conn.commit()

def get_detail_main():
    response = requests.get(query_list_url_gc)
    assert response.status_code == 200
    response = response.json()
    print('当前列表的个数为:',len(response))
    for index, item in enumerate(response):
        ID = item['ID']
        get_detail(ID, index)

def get_detail(ID, index):
    proxies = {}
    url = query_record_url_gc + ID
    response = requests.get(url, proxies=proxies)
    print('当前抓取的药品详情index:',index)
    assert response.status_code == 200
    response = response.json()
    response = [x['CONTENT'] for x in response]
    response.insert(0, ID)
    response = response[:-1]
    assert len(response) == 14
    sql = 'INSERT INTO `SYJ_GCYP_DETAIL` (ID,PZWH,CPMC,YWMC,SPM,JX,GG,SCDW,SCDZ,CPLB,PZRQ,YPZWH,YPBWM,YPBWMBZ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, tuple(response))
    conn.commit()

if __name__ == '__main__':
    get_detail_main()
