#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/20

import pymysql
import jieba
from jieba import Tokenizer
from jieba import posseg as pseg

MYSQL_CONF_MESH = {
    'host': '10.69.57.137',
    'port': 8096,
    'user': 'medical_vocabulary',
    'password': '152076',
    'db': 'medical_vocabulary',
    'charset': 'utf8',
}


def gen_dict_from_wanfang():
    db = pymysql.connect(**MYSQL_CONF_MESH)
    cursor = db.cursor()
    sql = 'SELECT name FROM wf_jb_ztclb'
    sql2 = 'SELECT name FROM wf_jpx_ztclb'
    cursor.execute(sql2)
    result = cursor.fetchall()
    print(len(result))
    names = set()
    for name in result:
        name = name[0].split(',')[0]
        if len(name) > 4:
            continue
        names.add(name)
    with open('wf_jpx_dict.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def fenci():
    # 加载自定义词典
    # jieba.load_userdict('wf_jb_dict_full.txt')
    # jieba.load_userdict('wf_jpx_dict_full.txt')
    # TODO 加载线上疾病库和ICD库，通过分词的方式做进一步优选
    jieba.set_dictionary('wf_jpx_dict.txt')
    result = jieba.cut('嗜酸细胞小肠炎')
    # print(list(result))
    print(dict(result))


################################################################
icd = '/Users/yaochao/Desktop/work_files/work2/ICD.xls'
online = '/Users/yaochao/Desktop/work_files/work2/online.csv'


def get_all_bodys():
    with open('jiepaocibiao.txt', 'r', encoding='utf-8') as f:
        all_bodys = f.readlines()
    all_bodys = [x.split('\n')[0] for x in all_bodys]
    return all_bodys


def get_all_illness():
    with open('wf_jb_dict.txt', 'r', encoding='utf-8') as f:
        all_illness = f.readlines()
    all_illness = [x.split('\n')[0] for x in all_illness]
    return all_illness


all_bodys = get_all_bodys()
all_illness = get_all_illness()


def get_body_illness(word=''):
    '''
    获取疾病和身体部位，两者之间有先后关系，先身体部位后疾病
    :param word:
    :return:
    '''
    max_body = 'None'
    max_body_len = -1
    for body in all_bodys:
        if body in word:
            if len(body) > max_body_len:
                max_body_len = len(body)
                max_body = body
    remain_word = word.replace(max_body, '{max_body}')
    max_illness = 'None'
    max_illness_len = -1
    for illness in all_illness:
        if illness in remain_word:
            if len(illness) > max_illness_len:
                max_illness_len = len(illness)
                max_illness = illness
    remain_word = remain_word.replace(max_illness, '{max_illness}')
    return word, max_body, max_illness, remain_word


def get_body_illness2(word=''):
    '''
    获取身体部位和疾病，两者之间是独立获取，没有任何关系
    :param word:
    :return:
    '''
    bodys = []
    tmp_word = word
    for body in all_bodys:
        if body in tmp_word:
            bodys.append(body)
            tmp_word = tmp_word.replace(body, '{{body{}}}'.format(len(bodys)))

    illnesses = []
    tmp_word2 = word
    for illness in all_illness:
        if illness in tmp_word2:
            illnesses.append(illness)
            tmp_word2 = tmp_word2.replace(illness, '{{illness{}}}'.format(len(illnesses)))

    return word, '|'.join(bodys), tmp_word, '|'.join(illnesses), tmp_word2


if __name__ == '__main__':
    word = '亚急性血行播散型肺结核'
    print(get_body_illness2(word))
