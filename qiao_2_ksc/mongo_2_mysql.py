#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/20


import pymongo
import pymysql
from pprint import pprint

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
    result_cursor = collection_detail.find().limit(1)
    counter = 0
    for i in result_cursor:
        # 进行字段提取和加工
        person = i['person']

        EMPI = person['ehrId']
        XM = person['pName']
        XZZ = person['addrCharPresent']
        HJDZ = person['addrCharRegi']
        LXDH = person['telNo']

        addrcodePresent = person['addrcodePresent']
        JTDZ1 = addrcodePresent[:2]
        JTDZ2 = addrcodePresent[:4]
        JTDZ3 = addrcodePresent[:6]
        JTDZ4 = addrcodePresent[:9]
        JTDZ5 = addrcodePresent[:12]  # TODO JTDZ5需要做映射 行政区划码到村子级别

        JDSQ = person['createUnit']
        JDRY = person['creator']
        JDRYMC = person['creatorName']
        JDRYID = person['creator']
        SQBM = person['createUnit']

        ZRYS = person['mainDoctorName']
        ZRYSID = person['mainDoctor']
        JDRQ = person['createDate']
        DAH = person['ehrId']
        BRDH = person['telNo']  # TODO 这里不明确
        SFZH = person['idNo']
        XB = person['sex']
        CSRQ = person['birthDate']
        LXRXM = person['contactPerson']
        LXRDH = person['contactTelNo']
        GZDW = person['workUnit']
        CZLX = person['householdFlag']
        MZ = person['nation']
        XX = person['bloodType']
        RH = person['rh']
        XL = person['eduLevel']
        ZYLB = person['occupation']

        marriage_map = {
            '1': '10',
            '2': '20',
            '3': '30',
            '4': '40',
            '5': '90',
        }
        HYZK = marriage_map[person['marriage']]

        ISET = person['feaChild']
        ISYCF = person['feaGravida']
        ISLNR = 0 if person['feaOlder'] == None else 1
        ISTNB = person['feaHyperg']
        ISGXY = person['feaHypert']
        ISJSB = person['feaPsy']
        ISFJH = person['feaPtb']
        ISPKRK = int(person['feaPap'])

        # sql拼装
        sql = 'INSERT INTO zjb_grda (EMPI,XM,XZZ,HJDZ,LXDH,JTDZ1,JTDZ2,JTDZ3,JTDZ4,JTDZ5,JDSQ,JDRY,JDRYMC,JDRYID,SQBM,ZRYS,ZRYSID,JDRQ,DAH,BRDH,SFZH,XB,CSRQ,LXRXM,LXRDH,GZDW,CZLX,MZ,XX,RH,XL,ZYLB,HYZK,ISET,ISYCF,ISLNR,ISTNB,ISGXY,ISJSB,ISFJH,ISPKRK) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (EMPI,XM,XZZ,HJDZ,LXDH,JTDZ1,JTDZ2,JTDZ3,JTDZ4,JTDZ5,JDSQ,JDRY,JDRYMC,JDRYID,SQBM,ZRYS,ZRYSID,JDRQ,DAH,BRDH,SFZH,XB,CSRQ,LXRXM,LXRDH,GZDW,CZLX,MZ,XX,RH,XL,ZYLB,HYZK,ISET,ISYCF,ISLNR,ISTNB,ISGXY,ISJSB,ISFJH,ISPKRK))
        # 每1000次循环，commit一次
        counter += 1
        if counter == 1:
            connect.commit()
            counter = 0




if __name__ == '__main__':
    main()
