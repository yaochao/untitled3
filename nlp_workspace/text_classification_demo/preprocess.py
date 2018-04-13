#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/9

from os import path
import xmltodict
from gzip import GzipFile
import pymysql
import jieba.posseg as pseg

# 原文链接：https://www.jianshu.com/p/e21b570a6b8a

STOPWORDS = '/Users/yaochao/python/datasets/stopwords/stopwords.txt'
stopwords = open(STOPWORDS, encoding='utf-8').read().split('\n')

base_path = '/Users/yaochao/python/datasets/downloads/sohu_news/'
news_path = path.join(base_path, 'news_sohusite_xml.xml.gz')
news_path_json = path.join(base_path, 'news_sohusite_xml_utf8.json')
mongo_config = {
    'host': '127.0.0.1',
    'port': 27017,
}
mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'datasets',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}


def text_preprocess():
    '''
    文本预处理
    将下载的原始数据进行转码，然后给文本标类别的标签，然后制作训练与测试数据，然后控制文本长度，分词，去标点符号
    :return:
    '''
    content = xmltodict.parse(GzipFile(news_path))
    # 写到文件里
    # content = json.dumps(content, ensure_ascii=False)
    # with open('news_sohusite_xml_utf8.json', mode='w', encoding='utf-8') as f:
    #     f.write(content)
    # # 存到MongoDB数据库
    # conn = pymongo.MongoClient(**mongo_config)
    # db = conn.get_database('datasets')
    # collection = db.get_collection('sohu_news')
    # for doc in content['root']['doc']:
    #     collection.insert(doc)
    # 存到MySQL数据库
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor()
    for doc in content['root']['doc']:
        sql = 'INSERT INTO sohu_news (url, docno, contenttitle, content) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, (doc['url'], doc['docno'], doc['contenttitle'], doc['content']))
        conn.commit()
    cursor.close()
    conn.close()


def text_analysis():
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM sohu_news WHERE category IS NOT NULL'
    cursor.execute(sql)
    print(cursor.fetchone())


def text_fenci():
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM sohu_news WHERE category IS NOT NULL AND content_fenci IS NULL AND category in ("business")'
    cursor.execute(sql)
    for item in cursor.fetchall():
        id = item['id']
        print(id)
        content = item['content']
        contenttitle = item['contenttitle']
        content = fenci_nostopwords(contenttitle + ' ' + content)
        sql = 'UPDATE sohu_news SET content_fenci=%s WHERE id=%s'
        cursor.execute(sql, (content, id))
        conn.commit()
    cursor.close()
    conn.close()


def fenci_nostopwords(text):
    words = pseg.cut(text)
    words2 = []
    for w in words:
        if w.flag != 'x':
            if w.word not in stopwords:
                words2.append(w.word)
    return ' '.join(words2)


if __name__ == '__main__':
    # text_preprocess()
    text_fenci()
