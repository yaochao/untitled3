#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/20


import pymongo
import pymysql
from pprint import pprint
import csv

MONGO_CONF = {
    'host': '127.0.0.1',
    'port': 27017,
}
MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'work',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}


def main():
    connect = pymysql.connect(**MYSQL_CONF)
    cursor = connect.cursor()

    client = pymongo.MongoClient(**MONGO_CONF)
    db = client.get_database('datasets')
    collection_detail = db.get_collection('xam_person_detail')
    result_cursor = collection_detail.find()
    counter = 0
    counter2 = 0
    for i in result_cursor:
        # 进行字段提取和加工
        person = i['person']
        # log progress..
        print(counter2, ' - ', i['_id'])

        EMPI = person['ehrId']
        # 支付方式
        YLFD = person['payMode']
        # 药物过敏 #TODO 多个的情况未考虑
        YWGM = ''
        YWGMBZ = None
        for i in person['ehrAllergyl']:
            YWGM = i['allergyId'] + ',' + YWGM
            YWGMBZ = i['otherAllergy']
        YWGM = YWGM if YWGM else None

        # 暴露史 #TODO 多个的情况未考虑, 为空情况
        BLS = ''
        for i in person['ehrExposure']:
            BLS = i['exposureId'] + ',' + BLS
        BLS = BLS if BLS else None

        # 既往史疾病 #TODO 多个的情况未考虑
        ehrPastSicks = person['ehrPastSicks']
        if ehrPastSicks:
            ehrPastSicks = ehrPastSicks[0]
            JWSRQ = ehrPastSicks['diagnosesDate']
            JWSJBBM = ehrPastSicks['optionId']
            JWSJBBZ = None
        else:
            JWSRQ = None
            JWSJBBM = None
            JWSJBBZ = None
        # 既往史手术 #TODO 多个的情况未考虑
        ehrPastOps = person['ehrPastOps'][0]
        JWSSSMC = ehrPastOps['pastName']
        JWSSSRQ = ehrPastOps['diagnosesDate']
        JWSSSBZ = None
        # 既往史外伤 #TODO 多个的情况未考虑
        ehrPastTraumas = person['ehrPastTraumas'][0]
        JWSWSMC = ehrPastTraumas['pastName']
        JWSWSRQ = ehrPastTraumas['diagnosesDate']
        JWSWSBZ = None
        # 既往史输血 #TODO 多个的情况未考虑
        ehrPastBloods = person['ehrPastBloods'][0]
        JWSSXYY = ehrPastBloods['bloodReason']
        JWSSXRQ = ehrPastBloods['diagnosesDate']
        JWSSXBZ = None

        # 家族史父亲 # TODO 应该使用ehrFamily
        father = i['father']
        JZSFQBM = father['optionId']
        JZSFQBZ = father['dieaseName']

        # 家族史母亲 # TODO 应该使用ehrFamily
        mother = i['mother']
        JZSMQBM = mother['optionId']
        JZSMQBZ = mother['dieaseName']

        # 家族史兄弟姐妹 # TODO 应该使用ehrFamily
        brother = i['brother']
        JZSXDJMBM = brother['optionId']
        JZSXDJMBM = None if JZSXDJMBM == '' else JZSXDJMBM
        JZSXDJMBZ = brother['dieaseName']

        # 家族史子女 # TODO 应该使用ehrFamily
        children = i['children']
        JZSZNBM = children['optionId']
        JZSZNBM = None if JZSZNBM == '' else JZSZNBM
        JZSZNBZ = children['dieaseName']

        # 遗传病
        genetic = person['ehrGenetic'] # 应该使用ehrGenetic
        if genetic:
            genetic = genetic[0]
            YCBSBM = genetic['optionId']
            YCBSBZ = genetic['diseaseName']
        else:
            YCBSBM = None
            YCBSBZ = None

        # 残疾情况 #TODO 多个的情况未考虑
        ehrDeformity = person['ehrDeformity'][0]
        CJQKBM = ehrDeformity['optionId']
        CJQKBZ = ehrDeformity['otherDisName']

        # 生活环境
        CFPFSS = person['kitchenExhaust']
        RLLX = person['fuelType']
        YS = person['waterCode']
        CS = person['wcType']
        QCL = person['livestockBar']

        # sql拼装
        sql = 'INSERT INTO zjb_grda_fz (EMPI, YLFD, YWGM, YWGMBZ,BLS,JWSJBBM,JWSRQ,JWSJBBZ,JWSSSMC,JWSSSRQ,JWSSSBZ,JWSWSMC,JWSWSRQ,JWSWSBZ,JWSSXYY,JWSSXRQ,JWSSXBZ,JZSFQBM,JZSFQBZ,JZSMQBM,JZSMQBZ,JZSXDJMBM,JZSXDJMBZ,JZSZNBM,JZSZNBZ,YCBSBM,YCBSBZ,CJQKBM,CJQKBZ,CFPFSS,RLLX,YS,CS,QCL) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (
            EMPI, YLFD, YWGM, YWGMBZ, BLS, JWSJBBM, JWSRQ,JWSJBBZ, JWSSSMC, JWSSSRQ, JWSSSBZ, JWSWSMC, JWSWSRQ, JWSWSBZ,
            JWSSXYY,
            JWSSXRQ, JWSSXBZ, JZSFQBM, JZSFQBZ, JZSMQBM, JZSMQBZ, JZSXDJMBM, JZSXDJMBZ, JZSZNBM, JZSZNBZ, YCBSBM,
            YCBSBZ,
            CJQKBM, CJQKBZ, CFPFSS, RLLX, YS, CS, QCL))
        # 每1000次循环，commit一次
        counter += 1
        counter2 += 1
        if counter == 1000:
            connect.commit()
            counter = 0

    # 最后别忘提交一次，提交最后不够1000个的insert操作。
    connect.commit()


if __name__ == '__main__':
    main()
