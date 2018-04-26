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
# 配置好 logging，gensim 会打印出日志
import logging
import os
import xlrd

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

base_path = '/Users/yaochao/python/datasets/'
userdict_path = os.path.join(base_path, 'user_dicts/online_and_icd_and_mesh.txt')
stopwords_path = os.path.join(base_path, 'user_dicts/stopwords5.txt')
file_path_100 = os.path.join(base_path, 'haodf_chats_detail_100W_pre.csv.word2vec_model')
file_path_1000 = os.path.join(base_path, 'haodf_chats_detail_1000W_pre.csv.word2vec_model')
file_path_1000_stopwords = os.path.join(base_path, 'haodf_chats_detail_1000W_pre.csv.w2v_model')
file_path_baike_cbow = os.path.join(base_path, 'downloads/cn.cbow.bin')
file_path_news_baidubaike_novel = os.path.join(base_path,
                                               'downloads/news_12g_baidubaike_20g_novel_90g_embedding_64.model')
file_path_news_baidubaike_novel_dim128 = '/Users/yaochao/python/datasets/downloads/news12g_bdbk20g_nov90g/news12g_bdbk20g_nov90g_dim128.bin'
file_path_baike_skipgram = os.path.join(base_path, 'downloads/cn.skipgram.bin')
file_path = os.path.join(base_path, 'abaike_10000.word2vec_model')
mysql_config = {
    'host': '127.0.0.1',
    # 'host': '172.31.48.29',
    'port': 8096,
    'user': 'spider',
    'password': '123456',
    'db': 'spider',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
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
        jieba.load_userdict(userdict_path)
        self.conn = pymysql.connect(**mysql_config)
        self.cursor = self.conn.cursor()
        sql = 'SELECT `content` FROM bw_news'
        self.cursor.execute(sql)
        self.stopwords = stopwordslist(stopwords_path)

    def __iter__(self):
        while True:
            try:
                item = self.cursor.fetchone()
                text = item['text']
                sentences = cut_sentence(text)
                for sentence in sentences:
                    words = list(jieba.cut(sentence))
                    words2 = []
                    for word in words:
                        if word not in self.stopwords:
                            words2.append(word)
                    yield words2
            except Exception:
                break

    def __del__(self):
        self.cursor.close()
        self.conn.close()


# train
def train_word2vec():
    start = time.time()
    sentences = MysentencesMySQL()
    model = gensim.models.Word2Vec(sentences=sentences, size=100, min_count=3)
    model.save(file_path)
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
    model_cbow = gensim.models.KeyedVectors.load_word2vec_format(fname=file_path_baike_cbow, binary=True, encoding='utf-8', unicode_errors='ignore')
    # model_skipgram = gensim.models.KeyedVectors.load_word2vec_format(fname=file_path_baike_skipgram, binary=True, encoding='utf-8', unicode_errors='ignore')
    model_100 = gensim.models.Word2Vec.load(file_path_100)
    model_1000 = gensim.models.Word2Vec.load(file_path_1000)
    model_1000_stopwords = gensim.models.Word2Vec.load(file_path_1000_stopwords)
    # model_news_baidubaike_novel = gensim.models.Word2Vec.load(file_path_news_baidubaike_novel_dim128)
    # model_news_baidubaike_novel = gensim.models.KeyedVectors.load_word2vec_format(fname=file_path_news_baidubaike_novel_dim128, binary=True, encoding='utf-8', unicode_errors='ignore')
    # print('你好' in model)
    word = '近视'
    print('100     ', model_100.wv.most_similar(word, topn=5))
    print('1000    ', model_1000.wv.most_similar(word, topn=5))
    print('1000sw  ', model_1000_stopwords.wv.most_similar(word, topn=5))
    print('baike   ', model_cbow.wv.most_similar(word, topn=5))
    # print('news_baidubaike_novel   ', model_news_baidubaike_novel.wv.most_similar(word, topn=5))
    # print(model.wv.similarity('中国', '北京'))
    # print(cos_similarity(model['中国'], model['北京']))


if __name__ == '__main__':
    use_model()
