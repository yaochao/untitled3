#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/9

from os import path
import xmltodict
from gzip import GzipFile
import pymysql
import jieba.posseg as pseg
import json

# 原文链接：https://www.jianshu.com/p/e21b570a6b8a
# 文本预处理
# 将下载的原始数据进行转码，然后给文本标类别的标签，然后制作训练与测试数据，然后控制文本长度，分词，去标点符号

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
    'passwd': 'toor',
    'db': 'datasets',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}


def text_import_mysql_mongo_file():
    '''
    xml导入 MySQL，MongoDB，File
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


def text_fenci_sohu_news():
    '''
    把文章字段进行分词，词语之间通过空格连接，然后更新到数据库对应的content_fenci字段。
    :return:
    '''
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


def text_fenci_bw_news():
    '''
    把文章字段进行分词，词语之间通过空格连接，然后更新到数据库对应的content_fenci字段。
    :return:
    '''
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    TAGS = {'高血压': 1, '糖尿病': 2, '儿童': 3, '孕产妇': 4, '中药': 5, '养生': 6}

    for tag in TAGS.keys():
        sql = 'SELECT id, news_article, news_title FROM bw_news WHERE news_tags=%s LIMIT 2000'
        cursor.execute(sql, (tag))
        while True:
            try:
                item = cursor.fetchone()
                id = item['id']
                print(id)
                news_article = item['news_article']
                items = json.loads(news_article)
                content = ''
                for i in items:
                    if i['type'] == 'newsPara':
                        content += i['content']

                news_title = item['news_title']
                content_fenci = fenci_nostopwords(news_title + ' ' + content)
                sql = 'UPDATE bw_news SET content_fenci=%s WHERE id=%s'
                cursor.execute(sql, (content_fenci, id))
                conn.commit()
            except:
                break
    cursor.close()
    conn.close()


def fenci_nostopwords(text):
    ''' 分词功能模块，去掉词性标注为x(标点符号等)的字符，去掉停用词 '''
    words = pseg.cut(text)
    words2 = []
    for w in words:
        if w.flag != 'x':
            if w.word not in stopwords:
                words2.append(w.word)
    return ' '.join(words2)


if __name__ == '__main__':
    text_fenci_bw_news()
