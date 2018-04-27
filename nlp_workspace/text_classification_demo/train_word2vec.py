#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/20


import csv
import time
import jieba
import gensim
import numpy as np
import pymysql
from numpy import linalg as la
from utils import cut_sentence
import logging
import os

# 配置好 logging，gensim 会打印出日志
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

base_path = '/Users/yaochao/python/datasets/'
userdict_path = os.path.join(base_path, 'user_dicts/online_and_icd_and_mesh.txt')
file_path_100 = os.path.join(base_path, 'haodf_chats_detail_100W_pre.csv.word2vec_model')
file_path_1000 = os.path.join(base_path, 'haodf_chats_detail_1000W_pre.csv.word2vec_model')
file_path_1000_stopwords = os.path.join(base_path, 'haodf_chats_detail_1000W_pre.csv.w2v_model')
file_path_baike_cbow = os.path.join(base_path, 'downloads/cn.cbow.bin')
file_path_news_baidubaike_novel = os.path.join(base_path,
                                               'downloads/news_12g_baidubaike_20g_novel_90g_embedding_64.model')
file_path_news_baidubaike_novel_dim128 = '/Users/yaochao/python/datasets/downloads/news12g_bdbk20g_nov90g/news12g_bdbk20g_nov90g_dim128.bin'
file_path_baike_skipgram = os.path.join(base_path, 'downloads/cn.skipgram.bin')

stopwords_path = os.path.join(base_path, 'stopwords/stopwords.txt')
model_path = os.path.join(base_path, 'bwnews_200dim_10000.w2v')
mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'toor',
    'db': 'datasets',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.SSDictCursor,
}


def preprocessing():
    '''
    数据预处理
    :return:
    '''
    start = time.time()
    with open('/Users/yaochao/python/corpus/haodf_chats_detail_all_pre.csv', mode='w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        filter_words = ['http://', '分享:', '通知:', '语音:', '微信 上传', 'javascript:;', '出停诊:', '患者上传的病例资料']
        with open('/Users/yaochao/python/corpus/haodf_chats_detail.csv', encoding='utf-8') as f2:
            f_csv2 = csv.reader(f2)
            index = 1
            for idx, line in enumerate(f_csv2):
                # if idx > 10000000:
                #     break
                line = line[1] if len(line) > 1 else ''
                has_filter_word = False
                for word in filter_words:
                    if word in line:
                        has_filter_word = True
                        break
                if not has_filter_word and len(line) > 10:
                    f_csv.writerow([index, line])
                    index += 1

    print('cost time: {}'.format(time.time() - start))


# NLP MAIN
class MysentencesFile(object):
    def __init__(self, filename):
        jieba.load_userdict(userdict_path)
        self.filename = filename
        self.stopwords = stopwordslist(stopwords_path)

    def __iter__(self):
        with open(self.filename, encoding='utf-8') as f:
            f_csv = csv.reader(f)
            for idx, sentence in f_csv:
                words = list(jieba.cut(sentence))
                words2 = []
                for word in words:
                    if word not in self.stopwords:
                        words2.append(word)
                yield words2


class MysentencesMySQL(object):
    def __init__(self):
        self.conn = pymysql.connect(**mysql_config)
        self.cursor = self.conn.cursor()
        sql = 'SELECT `content_fenci` FROM bw_news'
        # sql_random = 'SELECT `content_fenci` FROM bw_news WHERE id >= (SELECT FLOOR(RAND() * (SELECT MAX(id) FROM bw_news))) LIMIT 10000'
        self.cursor.execute(sql)
        self.stopwords = stopwordslist(stopwords_path)

    def __iter__(self):
        '''
        迭代器需要实现的方法: __iter__
        :return:
        '''
        item = self.cursor.fetchone()
        while item:
            content_fenci = item['content_fenci']
            words = content_fenci.split()
            words2 = []
            for word in words:
                if word not in self.stopwords:
                    words2.append(word)
            yield words2

            item = self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


# train
def train_word2vec():
    start = time.time()
    sentences = MysentencesMySQL()
    model = gensim.models.Word2Vec(sentences=sentences, size=200, min_count=3)
    model.save(model_path)
    print('cost time: {}'.format(time.time() - start))


# 余弦相似度
def cos_similarity(inA, inB):
    try:
        inA = np.mat(inA)
        inB = np.mat(inB)
        num = float(inA * inB.T)
        denom = la.norm(inA) * la.norm(inB)
        # return 0.5 + 0.5 * (num / denom) # 归一
        return num / denom
    except:
        return -1


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def use_model():
    # load the original Google word2vec model, use the KeyedVectors.load_word2vec_format()
    # print('你好' in model) 判断'你好'的词向量是否在model中。
    model = gensim.models.KeyedVectors.load_word2vec_format(fname=file_path_news_baidubaike_novel_dim128, binary=True, encoding='utf-8', unicode_errors='ignore')


    a = gensim.models.Word2Vec.load(model_path)
    word = '儿童'
    similar_word = model.wv.most_similar(word, topn=5)
    print('{}的近义词：{}'.format(word, similar_word))
    # print(model.wv.similarity('中国', '北京'))
    # print(cos_similarity(model['中国'], model['北京']))


if __name__ == '__main__':
    use_model()
