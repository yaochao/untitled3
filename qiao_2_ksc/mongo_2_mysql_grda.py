#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/20


import pymongo
import pymysql
from qiao_2_ksc import MYSQL_CONF_LOCAL, MYSQL_CONF_DEV, MONGO_CONF

# mysql
connect = pymysql.connect(**MYSQL_CONF_LOCAL)
cursor = connect.cursor()
# mongodb
client = pymongo.MongoClient(**MONGO_CONF)
db = client.get_database('datasets')
collection_detail = db.get_collection('xam_person_detail_514')


def main():
    result_cursor = collection_detail.find()
    counter = 0
    counter2 = 0
    for i in result_cursor:
        # 进行字段提取和加工
        person = i['person']

        BM = person['ehrId']
        XM = person['pName']
        XZZ = person['addrCharPresent']
        HJDZ = person['addrCharRegi']
        LXDH = person['telNo']

        addrcodePresent = person['ehrId']
        JTDZ1 = addrcodePresent[:2]
        JTDZ2 = addrcodePresent[:4]
        JTDZ3 = addrcodePresent[:6]
        JTDZ4 = addrcodePresent[:9]
        JTDZ5 = addrcodePresent[:12]

        JDSQ = person['createUnit']
        JDSQ = transfer_childhospital_to_roothospital(JDSQ)  # 没有账号的4家机构，映射到他的上级医院
        JDRY = person['creator']
        JDRYMC = person['creatorName']
        JDRYID = person['creator']
        SQBM = JDSQ

        ZRYS = person['mainDoctorName']
        ZRYSID = person['mainDoctor']
        JDRQ = person['createDate']
        DAH = person['ehrId']
        BRDH = person['telNo']  # TODO 这里不明确
        SFZH = person['idNo']
        XB = person['sex'] if person['sex'] else '9'
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
        HYZK = marriage_map[person['marriage']] if person['marriage'] else 90

        ISET = person['feaChild']
        ISYCF = person['feaGravida']
        ISLNR = 0 if person['feaOlder'] == None else 1
        ISTNB = person['feaHyperg']
        ISGXY = person['feaHypert']
        ISJSB = person['feaPsy']
        ISFJH = 0 if person['feaPtb'] == None else 1
        ISPKRK = int(person['feaPap'])

        # sql拼装
        sql = 'INSERT INTO sjzq_grda (bm,xm,xzz,hjdz,lxdh,jtdz1,jtdz2,jtdz3,jtdz4,jtdz5,jdsq,jdry,jdrymc,jdryid,sqbm,zrys,zrysid,jdrq,dah,brdh,sfzh,xb,csrq,lxrxm,lxrdh,gzdw,czlx,mz,xx,rh,xl,zylb,hyzk,iset,isycf,islnr,istnb,isgxy,isjsb,isfjh,ispkrk,prj) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (
            BM, XM, XZZ, HJDZ, LXDH, JTDZ1, JTDZ2, JTDZ3, JTDZ4, JTDZ5, JDSQ, JDRY, JDRYMC, JDRYID, SQBM, ZRYS, ZRYSID, JDRQ, DAH, BRDH, SFZH, XB, CSRQ, LXRXM, LXRDH, GZDW, CZLX, MZ, XX, RH, XL, ZYLB, HYZK, ISET, ISYCF, ISLNR, ISTNB, ISGXY, ISJSB, ISFJH, ISPKRK, 1))
        # 每1000次循环，commit一次
        counter += 1
        counter2 += 1
        if counter == 10000:
            connect.commit()
            counter = 0
        # log progress..
        print(counter2, '-', XM)
    # 最后别忘提交一次，提交最后不够10000个的insert操作。
    connect.commit()
    connect.close()


def transfer_childhospital_to_roothospital(createUnit):
    map_createUnit = {
        '152222001001': '152222001',
        '152222001002': '152222001',
        '152222001003': '152222001',
        '220180001001': '220180001',
    }
    if createUnit in map_createUnit.keys():
        return map_createUnit[createUnit]
    else:
        return createUnit


if __name__ == '__main__':
    main()
