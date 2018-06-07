#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/18
import time

import requests
import pymysql
import pymongo

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

user_pass_list = [
    ('科右中旗卫生局', 'xingjinhua', '123456789'),
    ('巴彦呼舒镇社区卫生服务中心', '152222001', '111111'),
    ('吐列毛杜', 'cyl', 'cyl537'),
    ('高力板', 'Wxp', '19751231'),
    ('巴彦淖尔', 'ysg', 'yu2008li'),
    ('杜尔基', 'hanbomin', '111111'),
    ('好腰苏木', '220150001', 'hbx18704864999'),
    ('新佳木', 'licheng', '111111'),
    ('代钦塔拉', 'liuch', '654321'),
    ('巴仁哲里木', 'mhj', '123456'),
    ('坤都冷', 'lfx111', '13654827241'),
    ('巴彦忙哈', 'hanguolin', '010203'),
    ('西日嘎', 'tjs', '111111'),
    ('巴仁太本', 'gaochangsui', '654321'),
    ('义和道卜', 'gwh1', '13948224598'),
    ('布敦化', 'baifengying', '27145156'),
    ('准太本', 'kxy', '111111'),
    ('巴扎拉嘎', 'suliyun', 'sly123'),
    ('额木庭高勒', 'bty', '1234567'),
    ('哈日诺尔', 'baohaimei', '222222'),
    ('扎木沁', 'jinlong', '123456789'),
    ('吐列毛杜农场', 'daixiaorong', '123123123'),
    ('布敦化牧场', 'wbl', 'wbl123456'),
    ('铜矿', 'zhengjing', '668800'),
    ('孟恩套力盖银铅矿职工医院', 'qkjfy', 'BNM291'),
]

connect = pymysql.connect(**MYSQL_CONF_DEV)

client = pymongo.MongoClient(**MONGO_CONF)
db = client['datasets']
collection_list_518 = db['xam_person_list_518']


####################### 登录，返回session #######################
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
        print('登录异常')


def login_xjh():
    session = login('xingjinhua', '123456789')
    return session


SESSION_xjh = login_xjh()


####################### 抓取大区，插入MySQL #######################
def get_dq(session, region_code="152222"):
    try:
        response = session.get(
            url="http://jkda.xamwjw.gov.cn/ph/queryDsnTree.action",
            params={
                "_dc": "1525946535905",
                "id": region_code,
                "jsonResult": "true",
            },
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "Host": "jkda.xamwjw.gov.cn",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "http://jkda.xamwjw.gov.cn/loadTpl.action?tplId=Hr_pi&tplScript=hr,IdCardNoCheck",
            },
        )
        dsnTreeList = response.json()['dsnTreeList']
        return dsnTreeList
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def insert_dq():
    # Mysql
    print('正在抓取大区...')
    cursor = connect.cursor()
    # 兴安盟县下面的镇列表
    session = login('xingjinhua', '123456789')
    dsnTreeList = get_dq(session=session, region_code='152222')
    print(dsnTreeList)
    sql = 'INSERT INTO sjzq_dq (bm,mc,sjbm,lx,prj) VALUES (%s, %s, %s, %s, %s)'
    for i in dsnTreeList:
        town_id = i['id']
        town_text = i['text']
        cursor.execute(sql, (town_id, town_text, '152222', '5', '1'))
        dsnTreeList2 = get_dq(session=session, region_code=town_id)
        for ii in dsnTreeList2:
            village_id = ii['id']
            village_text = ii['text']
            cursor.execute(sql, (village_id, village_text, town_id, '5', '1'))
        connect.commit()
    cursor.close()
    print('抓取大区完成.')


####################### 抓取机构，插入MySQL #######################
def get_jg(session):
    # 启奥系统 - 机构
    # POST http://jkda.xamwjw.gov.cn/org/queryOrganizationTreeForOrgList.action

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/org/queryOrganizationTreeForOrgList.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "orgInfo.orgStatus": "",
                "node": "root",
                "orgInfo.orgCode": "",
                "jsonResult": "true",
                "orgInfo.createPeople": "",
                "orgInfo.orgName": "",
                "orgInfo.orgType": "",
            },
        )
        return response.json()

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def insert_jg():
    # mysql
    print('正在抓取机构...')
    cursor = connect.cursor()
    # get
    session = login('xingjinhua', '123456789')
    r = get_jg(session)
    children = r['children'][0]['children'][0]['children']
    type_map = {
        u"盟/市卫生局": '1',
        u"区/县卫生局": '2',
        u"卫生服务中心/卫生院": '4',
        u"卫生服务站/卫生室": '5',
    }
    sql = 'INSERT INTO sjzq_jg (bm,mc,sjbm,state,lx,prj) VALUES (%s,%s,%s,%s,%s,%s)'
    for i in children:
        SJBM = '152222000'
        BM = i['orgCode']
        if BM.startswith('22'):
            BM = '1522' + BM
        MC = i['orgName']
        LX = type_map[i['orgType']]
        children = i['children']
        cursor.execute(sql, (BM, MC, SJBM, '1', LX, '1'))
        if children:
            for ii in children:
                SJBM = BM
                BM = ii['orgCode']
                if BM.startswith('22'):
                    BM = '1522' + BM
                MC = ii['orgName']
                LX = type_map[ii['orgType']]
                cursor.execute(sql, (BM, MC, SJBM, '1', LX, '1'))
    connect.commit()
    cursor.close()
    print('抓取机构完成...')


####################### 抓取科室，插入MySQL #######################
def get_ks(session):
    # 启奥系统 - 科室
    # POST http://jkda.xamwjw.gov.cn/dept/queryDeptByParams.action

    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/dept/queryDeptByParams.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "dept.deptName": "",
                "start": "0",
                "dept.deptType": "",
                "limit": "10000",
                "jsonResult": "true",
                "page": "1",
                "dept.deptCode": "",
            },
        )
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def insert_ks():
    # mysql
    cursor = connect.cursor()
    cursor2 = connect.cursor()
    # get
    for i in user_pass_list:
        name = i[0]
        print('正在抓取科室: %s' % name)
        username = i[1]
        password = i[2]
        session = login(username, password)
        result = get_ks(session=session)
        sql = 'INSERT INTO sjzq_ks (sqbm,bm,mc,state,prj) VALUES (%s,%s,%s,%s,%s)'
        for i in result['pageResult']['pages']:
            ORG_NAME = i['ORG_NAME']
            sql2 = 'SELECT BM FROM sjzq_jg WHERE MC=%s'
            cursor2.execute(sql2, (ORG_NAME))
            result = cursor2.fetchone()
            BM = result['BM']
            DEPT_ID = i['DEPT_ID']
            DEPT_NAME = i['DEPT_NAME']
            state = 1
            prj = 1
            cursor.execute(sql, (BM, DEPT_ID, DEPT_NAME, state, prj))
    connect.commit()
    cursor.close()
    cursor2.close()
    print('抓取科室完成.')


####################### 抓取人员，插入MySQL #######################
def get_ry_list(session):
    '''
    获取人员列表
    :param session:
    :return:
    '''
    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/orguser/queryUserByParams.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "orgUserBean.sex": "",
                "page": "1",
                "orgUserBean.orgperStatus": "",
                "start": "0",
                "orgUserBean.technicTitle": "",
                "orgUserBean.positionCode": "",
                "limit": "1000",
                "jsonResult": "true",
                "orgUserBean.empName": "",
                "orgUserBean.idNo": "",
                "orgUserBean.deptId": "",
            },
        )
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_ry_detail(session, EMPID):
    # 启奥系统 - 人员详情
    # POST http://jkda.xamwjw.gov.cn/orguser/queryEntity.action
    try:
        response = session.post(
            url="http://jkda.xamwjw.gov.cn/orguser/queryEntity.action",
            headers={
                "Origin": "http://jkda.xamwjw.gov.cn",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Referer": "http://jkda.xamwjw.gov.cn/main.action",
                "Host": "jkda.xamwjw.gov.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "empId": EMPID,
                "jsonResult": "true",
            },
        )
        return response.json()
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def insert_ry():
    # mysql
    cursor = connect.cursor()
    # for
    for i in user_pass_list:
        name = i[0]
        print('正在抓取人员: %s' % name)
        username = i[1]
        password = i[2]
        session = login(username, password)
        # get doctor list
        result = get_ry_list(session=session)
        sql = 'INSERT INTO sjzq_ry (sqbm,bm,mc,xb,lb,ksbm,state,csrq,sfzh,lxdh,prj) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for i in result['pageResult']['pages']:
            EMPID = i['EMPID']
            # get doctor detail
            result = get_ry_detail(session, EMPID)
            orgUserBean = result['orgUserBean']

            sqbm = result['orgCode']
            if sqbm.startswith('22'):
                sqbm = '1522' + sqbm
            bm = orgUserBean['empId']
            mc = orgUserBean['empName']
            xb = orgUserBean['sex'] if orgUserBean['sex'] else '0'
            lb = '1' if orgUserBean['perType'] else '2'
            ksbm = orgUserBean['deptId']
            state = '1'
            csrq = orgUserBean['birthDate']
            sfzh = orgUserBean['idNo']
            lxdh = orgUserBean['telNo']
            prj = '1'
            cursor.execute(sql, (sqbm, bm, mc, xb, lb, ksbm, state, csrq, sfzh, lxdh, prj))
        connect.commit()
    cursor.close()
    print('抓取人员完成.')


####################### 抓取个人档案插入Mongo，然后插入MySQL #######################
def get_person_list(session):
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
                "page": "%s" % 1,
                "start": "%s" % 0,
                "limit": "%s" % 210000,
                "parameter.dsn": "",
            },
        )
        page_data = response.json()['resultData']['pageData']
        for i in page_data:
            i['_id'] = i['SERIAL_CODE']
            collection_list_518.insert(i)
    except Exception as e:
        print('个人档案列表请求失败 %s' % e)


def get_person_detail(serial_code, session):
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
                "jsonResult": "true",
                "serialCode": "%s" % serial_code,
                "peId": "%s" % serial_code,
            },
        )
        person_ehr = response.json()
        return person_ehr
    except Exception as e:
        print('个人档案详细信息请求失败:%s  serial_code:%s' % (e, serial_code))


def transfer_childhospital_to_roothospital(createUnit):
    '''
    把没有账号的那四家医院的编码转为他的上级医院的编码
    :param createUnit:
    :return:
    '''
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


def batch_insert_person_detail(items):
    '''
    批量转换个人档案到MySQL
    :param items:
    :return:
    '''
    # 插入个人档案表（基本信息）：sjzq_grda
    cursor = connect.cursor()
    for i in items:
        # i 必须是字典，'person'必须在字典的key，person对应的字典的value不能为None
        if type(i) != dict or 'person' not in i.keys() or not i['person']:
            print(i)
            print('不是正确的个人档案数据，不插入MySQL')
            continue

        person = i['person']

        BM = person['ehrId']
        XM = person['pName']
        XZZ = person['addrCharPresent']
        HJDZ = person['addrCharRegi']
        LXDH = person['telNo']

        # person['addrcodePresent'] 并且判断为空为汉字的情况。如果为空为汉字，那么就是用person['ehrId']
        try:
            addrcodePresent = int(person['addrcodePresent'])
            addrcodePresent = str(addrcodePresent)
        except:
            addrcodePresent = person['ehrId']
        JTDZ1 = addrcodePresent[:2]
        JTDZ2 = addrcodePresent[:4]
        JTDZ3 = addrcodePresent[:6]
        JTDZ4 = addrcodePresent[:9]
        JTDZ5 = addrcodePresent[:12]

        JDSQ = person['createUnit']
        if JDSQ.startswith('22'):  # 把开头为22的机构，补充上1522。
            JDSQ = '1522' + JDSQ
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

        RH = person['rh']  # RH TODO 阴性阳性映射
        map_RH = {
            '1': '2',
            '2': '1',
            '3': '3',
        }
        if RH in map_RH:
            RH = map_RH[RH]

        XL = person['eduLevel']  # TODO 学历映射
        map_XL = {
            '1': '9',
            '2': '8',
            '3': '7',
            '4': '6',
            '5': '3',
            '6': '10',
            '7': '5',
            '8': '4',
            '9': '2',
            '10': '1',
        }
        if XL in map_XL:
            XL = map_XL[str(XL)]

        ZYLB = person['occupation']  # TODO 职业类别
        if ZYLB:
            ZYLB = str(int(ZYLB) - 1)

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
        ISLNR = 1 if person['feaOlder'] == 1 else 0
        ISTNB = person['feaHyperg']
        ISGXY = person['feaHypert']
        ISJSB = person['feaPsy']
        ISFJH = 1 if person['feaPtb'] == 1 else 0
        ISPKRK = int(person['feaPap'])

        # sql拼装
        sql = 'INSERT INTO sjzq_grda (bm,xm,xzz,hjdz,lxdh,jtdz1,jtdz2,jtdz3,jtdz4,jtdz5,jdsq,jdry,jdrymc,jdryid,sqbm,zrys,zrysid,jdrq,dah,brdh,sfzh,xb,csrq,lxrxm,lxrdh,gzdw,czlx,mz,xx,rh,xl,zylb,hyzk,iset,isycf,islnr,istnb,isgxy,isjsb,isfjh,ispkrk,prj) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (
            BM, XM, XZZ, HJDZ, LXDH, JTDZ1, JTDZ2, JTDZ3, JTDZ4, JTDZ5, JDSQ, JDRY, JDRYMC, JDRYID, SQBM, ZRYS, ZRYSID,
            JDRQ, DAH, BRDH, SFZH, XB, CSRQ, LXRXM, LXRDH, GZDW, CZLX, MZ, XX, RH, XL, ZYLB, HYZK, ISET, ISYCF, ISLNR,
            ISTNB, ISGXY, ISJSB, ISFJH, ISPKRK, 1))
    connect.commit()
    cursor.close()

    # 插入个人档案多选纵表和既往史多选纵表
    sql0 = 'INSERT INTO sjzq_grda_dxzb (jmbm,lx,sublx,bm,bz,prj) VALUES (%s,%s,%s,%s,%s,%s)'
    sql1 = 'INSERT INTO sjzq_grda_dxzb (jmbm,lx,bm,bz,prj) VALUES (%s,%s,%s,%s,%s)'
    sql2 = 'INSERT INTO sjzq_grda_dxzb (jmbm,lx,bm,prj) VALUES (%s,%s,%s,%s)'
    sql3 = 'INSERT INTO sjzq_grda_jwsdxzb (jmbm,lx,bm,mc,rq,bz,prj) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    sql4 = 'INSERT INTO sjzq_grda_jwsdxzb (jmbm,lx,mc,rq,bz,prj) VALUES (%s,%s,%s,%s,%s,%s)'
    cursor = connect.cursor()
    for i in items:
        # 进行字段提取和加工
        person = i['person']
        BM = person['ehrId']
        PRJ = 1

        # 支付方式
        YLFD = person['payMode']
        if YLFD:
            LX = 1
            YLFDs = YLFD.split('/')
            for i in YLFDs:
                if i == '8':
                    otherPayMode = person['otherPayMode']
                else:
                    otherPayMode = None
                cursor.execute(sql1, (BM, LX, i, otherPayMode, PRJ))

        # 药物过敏
        ehrAllergyl = person['ehrAllergyl']
        if ehrAllergyl:
            LX = 2
            for i in ehrAllergyl:
                allergyId = i['allergyId']
                otherAllergy = i['otherAllergy']
                cursor.execute(sql1, (BM, LX, allergyId, otherAllergy, PRJ))

        # 暴露史
        ehrExposure = person['ehrExposure']
        if ehrExposure:
            LX = 3
            for i in ehrExposure:
                exposureId = i['exposureId']
                cursor.execute(sql1, (BM, LX, exposureId, None, PRJ))

        # 家族史
        ehrFamily = person['ehrFamily']
        if ehrFamily:
            LX = 4
            for i in ehrFamily:
                relaId = i['relaId']  # 1.父亲 2.母亲 3.兄弟姐妹 4.子女
                optionId = i['optionId']  # 选项id
                if optionId == '12':  # 疾病选择其他时，记录具体疾病名称
                    dieaseName = i['dieaseName']
                else:
                    dieaseName = None
                cursor.execute(sql0, (BM, LX, relaId, optionId, dieaseName, PRJ))

        # 遗传疾病
        ehrGenetic = person['ehrGenetic']
        if ehrGenetic:
            LX = 5
            for i in ehrGenetic:
                optionId = i['optionId']  # 选项id
                if optionId == '2':  # 选择2时，记录具体疾病名称。
                    dieaseName = i['diseaseName']
                else:
                    dieaseName = None
                cursor.execute(sql1, (BM, LX, optionId, dieaseName, PRJ))

        # 残疾情况
        ehrDeformity = person['ehrDeformity']
        if ehrDeformity:
            LX = 6
            for i in ehrDeformity:
                optionId = i['optionId']
                if optionId == '8':
                    otherDisName = i['otherDisName']
                else:
                    otherDisName = None
                cursor.execute(sql1, (BM, LX, optionId, otherDisName, PRJ))

        # 厨房排风设施
        kitchenExhaust = person['kitchenExhaust']
        if kitchenExhaust:
            kitchenExhaust = kitchenExhaust.split('/')
            LX = 7
            for i in kitchenExhaust:
                cursor.execute(sql2, (BM, LX, i, PRJ))

        # 燃料类型
        fuelType = person['fuelType']
        if fuelType:
            fuelType = fuelType.split('/')
            LX = 8
            for i in fuelType:
                cursor.execute(sql2, (BM, LX, i, PRJ))

        # 饮水
        waterCode = person['waterCode']
        if waterCode:
            waterCode = waterCode.split('/')
            LX = 9
            for i in waterCode:
                cursor.execute(sql2, (BM, LX, i, PRJ))

        # 厕所
        wcType = person['wcType']
        if wcType:
            wcType = wcType.split('/')
            LX = 10
            for i in wcType:
                cursor.execute(sql2, (BM, LX, i, PRJ))

        # 禽畜栏
        livestockBar = person['livestockBar']
        if livestockBar:
            livestockBar = livestockBar.split('/')
            LX = 11
            for i in livestockBar:
                i = int(i) + 1  # 禽畜栏这个选项和其他的选项不一样，他是从0开始的，所以需要+1，保持和规定的同步
                cursor.execute(sql2, (BM, LX, i, PRJ))

        # 既往史疾病
        ehrPastSicks = person['ehrPastSicks']
        if ehrPastSicks:
            LX = 1
            MC_list = [u'无', u'高血压', u'糖尿病', u'冠心病', u'慢性阻塞性肺病', u'恶性肿瘤', u'脑卒中', u'严重精神障碍', u'肺结核', u'肝炎', u'其他法定传染病',
                       u'职业病',
                       u'其他']
            for i in ehrPastSicks:
                optionId = i['optionId']
                diagnosesDate = i['diagnosesDate']
                pastName = i['pastName']
                MC = MC_list[int(optionId) - 1]
                if MC == u'无':
                    continue
                cursor.execute(sql3, (BM, LX, optionId, MC, diagnosesDate, pastName, PRJ))

        # 既往史手术
        ehrPastOps = person['ehrPastOps']
        if ehrPastOps:
            LX = 2
            for i in ehrPastOps:
                optionId = i['optionId']
                pastName = i['pastName']
                diagnosesDate = i['diagnosesDate']
                BZ = None
                # 选择第一个选项"无"不插入
                # 疾病名称为"无"不插入
                if pastName == u'无' or optionId == '1':
                    continue
                # 疾病名和诊断日期必须有一个才插入
                if pastName or diagnosesDate:
                    cursor.execute(sql4, (BM, LX, pastName, diagnosesDate, BZ, PRJ))

        # 既往史外伤
        ehrPastTraumas = person['ehrPastTraumas']
        if ehrPastTraumas:
            LX = 3
            for i in ehrPastTraumas:
                optionId = i['optionId']
                pastName = i['pastName']
                diagnosesDate = i['diagnosesDate']
                BZ = None
                # 选择第一个选项"无"不插入
                # 疾病名称为"无"不插入
                if pastName == u'无' or optionId == '1':
                    continue
                # 疾病名和诊断日期必须有一个才插入
                if pastName or diagnosesDate:
                    cursor.execute(sql4, (BM, LX, pastName, diagnosesDate, BZ, PRJ))

        # 既往史输血
        ehrPastBloods = person['ehrPastBloods']
        if ehrPastBloods:
            LX = 4
            for i in ehrPastBloods:
                optionId = i['optionId']
                bloodReason = i['bloodReason']
                diagnosesDate = i['diagnosesDate']
                BZ = None
                # 选择第一个选项"无"不插入
                # 疾病名称为"无"不插入
                if bloodReason == u'无' or optionId == '1':
                    continue
                # 疾病名和诊断日期必须有一个才插入
                if bloodReason or diagnosesDate:
                    cursor.execute(sql4, (BM, LX, bloodReason, diagnosesDate, BZ, PRJ))
    connect.commit()
    cursor.close()


def get_insert_all_person_detail():
    '''
    获取所有的人员的详细信息，并且插入到MySQL中。
    :return:
    '''
    global SESSION_xjh
    if not SESSION_xjh:
        SESSION_xjh = login_xjh()
    cursor = collection_list_518.find({}, {"_id": 1}).limit(50000)
    all_serial_code = [x['_id'] for x in cursor]
    tmp_1000_person_detail = []  # 临时存放1000个人的详细信息，满1000，批量转换到MySQL一次。
    while all_serial_code:
        serial_code = all_serial_code.pop()
        person_ehr = get_person_detail(serial_code, SESSION_xjh)
        if not person_ehr:
            print('serial_code %s got None result' % serial_code)
            continue
        if 'sessionInvalid' in person_ehr.keys():
            print(person_ehr['sessionInvalid'])
            SESSION_xjh = login_xjh()
            print('登录信息过期，重新登录成功')
            all_serial_code.append(serial_code)
        tmp_1000_person_detail.append(person_ehr)
        print('剩余:%s' % len(all_serial_code))
        # 插入MySQL
        if len(tmp_1000_person_detail) >= 1000:
            batch_insert_person_detail(tmp_1000_person_detail)
            tmp_1000_person_detail[:] = []

    # 最后不够1000个，再插入一次
    batch_insert_person_detail(tmp_1000_person_detail)


####################### 把个人档案里面责任医生和建档人员，有姓名没有ID的，新建到人员表 #######################
def create_ry():
    '''
    创建人员
    :return:
    '''
    all_set = set()
    cursor = connect.cursor()
    sql = 'SELECT sqbm, jdrymc FROM sjzq_grda where jdryid is null and jdrymc is not null'
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        sqbm = i['sqbm']
        jdrymc = i['jdrymc']
        all_set.add((sqbm, jdrymc))

    sql2 = 'SELECT sqbm, zrys FROM sjzq_grda where zrysid is null and zrys is not null'
    cursor.execute(sql2)
    result = cursor.fetchall()
    for i in result:
        sqbm = i['sqbm']
        zrys = i['zrys']
        all_set.add((sqbm, zrys))

    print('一共需要新建人员: %s' % len(all_set))
    for index, i in enumerate(all_set):
        sqbm = i[0]
        zrys = i[1]
        bm = sqbm + 'A' + str(index)
        state = 1
        prj = 1
        print('正在新建人员第: %s' % index)
        sql = 'INSERT INTO sjzq_ry (sqbm, bm, mc, state, prj) values (%s,%s,%s,%s,%s)'
        cursor.execute(sql, (sqbm, bm, zrys, state, prj))
    connect.commit()
    cursor.close()


def update_ry_to_grda():
    '''
    把创建的人员更新到个人档案对应的建档人员和责任医生
    :return:
    '''
    cursor = connect.cursor()
    sql = 'SELECT * FROM sjzq_ry'
    cursor.execute(sql)
    result = cursor.fetchall()
    l = len(result)
    for index, i in enumerate(result):
        print("正在更新个人档案,剩余: %s" % (l - index))
        sql = 'UPDATE sjzq_grda SET zrysid=%s WHERE sqbm=%s AND zrys=%s AND zrysid is null'
        sql2 = 'UPDATE sjzq_grda SET jdryid=%s,jdry=%s WHERE sqbm=%s AND jdrymc=%s AND jdryid is null'
        cursor.execute(sql, (i['bm'], i['sqbm'], i['mc']))
        cursor.execute(sql2, (i['bm'], i['bm'], i['sqbm'], i['mc']))
        connect.commit()
    cursor.close()


def main():
    start = time.time()
    # insert_dq()
    # insert_jg()
    # insert_ks()
    # insert_ry()
    # get_person_list(SESSION_xjh)
    # get_insert_all_person_detail()
    create_ry()
    update_ry_to_grda()
    # connect.close()
    print('总共耗时: %s' % (time.time() - start))


if __name__ == '__main__':
    main()
