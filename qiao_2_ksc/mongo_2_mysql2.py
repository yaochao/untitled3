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
    'passwd': 'toor',
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
    # result_cursor = collection_detail.find({"_id": "2762"})
    result_cursor = collection_detail.find()
    counter = 0
    for i in result_cursor:

        # log progress..
        counter += 1
        print(counter, ' - ', i['_id'])

        # 进行字段提取和加工
        person = i['person']
        EMPI = person['ehrId']
        PRJ = 1

        # 支付方式
        YLFD = person['payMode']
        if YLFD:
            LX = 1
            YLFDs = YLFD.split('/')
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,BZ,PRJ) VALUES (%s,%s,%s,%s,%s)'
            for i in YLFDs:
                if i == '8':
                    otherPayMode = person['otherPayMode']
                else:
                    otherPayMode = None
                cursor.execute(sql, (EMPI, LX, i, otherPayMode, PRJ))

        # 药物过敏
        ehrAllergyl = person['ehrAllergyl']
        if ehrAllergyl:
            LX = 2
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,BZ,PRJ) VALUES (%s,%s,%s,%s,%s)'
            for i in ehrAllergyl:
                allergyId = i['allergyId']
                otherAllergy = i['otherAllergy']
                cursor.execute(sql, (EMPI, LX, allergyId, otherAllergy, PRJ))

        # 暴露史
        ehrExposure = person['ehrExposure']
        if ehrExposure:
            LX = 3
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,BZ,PRJ) VALUES (%s,%s,%s,%s,%s)'
            for i in ehrExposure:
                exposureId = i['exposureId']
                cursor.execute(sql, (EMPI, LX, exposureId, None, PRJ))

        # 家族史
        ehrFamily = person['ehrFamily']
        if ehrFamily:
            LX = 4
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,SUBLX,BM,BZ,PRJ) VALUES (%s,%s,%s,%s,%s,%s)'
            for i in ehrFamily:
                relaId = i['relaId']  # 1.父亲 2.母亲 3.兄弟姐妹 4.子女
                optionId = i['optionId']  # 选项id
                if optionId == '12':  # 疾病选择其他时，记录具体疾病名称
                    dieaseName = i['dieaseName']
                else:
                    dieaseName = None
                cursor.execute(sql, (EMPI, LX, relaId, optionId, dieaseName, PRJ))

        # 遗传疾病
        ehrGenetic = person['ehrGenetic']
        if ehrGenetic:
            LX = 5
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,BZ,PRJ) VALUES (%s,%s,%s,%s,%s)'
            for i in ehrGenetic:
                optionId = i['optionId']  # 选项id
                if optionId == '2':  # 选择2时，记录具体疾病名称。TODO 这里的选项与我们的选项个数不符。他有2项，我们好像有6项。需要做映射
                    dieaseName = i['diseaseName']
                else:
                    dieaseName = None
                cursor.execute(sql, (EMPI, LX, optionId, dieaseName, PRJ))

        # 残疾情况
        ehrDeformity = person['ehrDeformity']
        if ehrDeformity:
            LX = 6
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,BZ,PRJ) VALUES (%s,%s,%s,%s,%s)'
            for i in ehrDeformity:
                optionId = i['optionId']
                if optionId == '8':
                    otherDisName = i['otherDisName']
                else:
                    otherDisName = None
                cursor.execute(sql, (EMPI, LX, optionId, otherDisName, PRJ))

        # 厨房排风设施
        kitchenExhaust = person['kitchenExhaust']
        if kitchenExhaust:
            kitchenExhaust = kitchenExhaust.split('/')
            LX = 7
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,PRJ) VALUES (%s,%s,%s,%s)'
            for i in kitchenExhaust:
                cursor.execute(sql, (EMPI, LX, i, PRJ))

        # 燃料类型
        fuelType = person['fuelType']
        if fuelType:
            fuelType = fuelType.split('/')
            LX = 8
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,PRJ) VALUES (%s,%s,%s,%s)'
            for i in fuelType:
                cursor.execute(sql, (EMPI, LX, i, PRJ))

        # 饮水
        waterCode = person['waterCode']
        if waterCode:
            waterCode = waterCode.split('/')
            LX = 9
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,PRJ) VALUES (%s,%s,%s,%s)'
            for i in waterCode:
                cursor.execute(sql, (EMPI, LX, i, PRJ))

        # 厕所
        wcType = person['wcType']
        if wcType:
            wcType = wcType.split('/')
            LX = 10
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,PRJ) VALUES (%s,%s,%s,%s)'
            for i in wcType:
                cursor.execute(sql, (EMPI, LX, i, PRJ))

        # 禽畜栏
        livestockBar = person['livestockBar']
        if livestockBar:
            livestockBar = livestockBar.split('/')
            LX = 11
            sql = 'INSERT INTO zjb_grda_fz_tyddd (EMPI,LX,BM,PRJ) VALUES (%s,%s,%s,%s)'
            for i in livestockBar:
                cursor.execute(sql, (EMPI, LX, i, PRJ))

        # 既往史疾病
        ehrPastSicks = person['ehrPastSicks']
        if ehrPastSicks:
            LX = 1
            MC_list = ['无','高血压','糖尿病','冠心病','慢性阻塞性肺病','恶性肿瘤','脑卒中','严重精神障碍','肺结核','肝炎','其他法定传染病','职业病','其他']
            sql = 'INSERT INTO zjb_grda_fz_jwsddd (EMPI,LX,BM,MC,RQ,BZ,PRJ) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            for i in ehrPastSicks:
                optionId = i['optionId']
                diagnosesDate = i['diagnosesDate']
                pastName = i['pastName']
                MC = MC_list[int(optionId)-1]
                cursor.execute(sql, (EMPI, LX, optionId, MC, diagnosesDate, pastName, PRJ))

        # 既往史手术
        ehrPastOps = person['ehrPastOps']
        if ehrPastOps:
            LX = 2
            sql = 'INSERT INTO zjb_grda_fz_jwsddd (EMPI,LX,BM,MC,RQ,BZ,PRJ) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            for i in ehrPastOps:
                optionId = i['optionId']
                pastName = i['pastName']
                diagnosesDate = i['diagnosesDate']
                BZ = None  # TODO 既往史手术无备注字段
                cursor.execute(sql, (EMPI, LX, optionId, pastName, diagnosesDate, BZ, PRJ))

        # 既往史外伤
        ehrPastTraumas = person['ehrPastTraumas']
        if ehrPastTraumas:
            LX = 3
            sql = 'INSERT INTO zjb_grda_fz_jwsddd (EMPI,LX,BM,MC,RQ,BZ,PRJ) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            for i in ehrPastTraumas:
                optionId = i['optionId']
                pastName = i['pastName']
                diagnosesDate = i['diagnosesDate']
                BZ = None  # TODO 既往史外伤无备注字段
                cursor.execute(sql, (EMPI, LX, optionId, pastName, diagnosesDate, BZ, PRJ))

        # 既往史输血
        ehrPastBloods = person['ehrPastBloods']
        if ehrPastBloods:
            LX = 4
            sql = 'INSERT INTO zjb_grda_fz_jwsddd (EMPI,LX,BM,MC,RQ,BZ,PRJ) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            for i in ehrPastBloods:
                optionId = i['optionId']
                bloodReason = i['bloodReason']
                diagnosesDate = i['diagnosesDate']
                BZ = None  # TODO 既往史输血无备注字段
                cursor.execute(sql, (EMPI, LX, optionId, bloodReason, diagnosesDate, BZ, PRJ))

        # 每1000次commit一次
        if counter % 1000 == 0:
            connect.commit()

    # 最后提交一次，最后不够1000的
    connect.commit()
    connect.close()


if __name__ == '__main__':
    main()
