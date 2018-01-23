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

import xlrd

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

base_path = '/Users/yaochao/python/datasets/'
userdict_path = base_path + 'user_dicts/online_and_icd_and_mesh.txt'
stopwords_path = base_path + 'user_dicts/stopwords5.txt'
file_path_100 = base_path + 'haodf_chats_detail_100W_pre.csv.word2vec_model'
file_path_1000 = base_path + 'haodf_chats_detail_1000W_pre.csv.word2vec_model'
file_path_1000_stopwords = base_path + 'haodf_chats_detail_1000W_pre.csv.w2v_model'
file_path_baike_cbow = base_path + 'downloads/cn.cbow.bin'
file_path_baike_skipgram = base_path + 'downloads/cn.skipgram.bin'
# file_path = base_path + 'abaike_10000.word2vec_model'
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
class Mysentences_file(object):
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


class Mysentences_mysql(object):
    def __init__(self):
        jieba.load_userdict(userdict_path)
        self.conn = pymysql.connect(**mysql_config)
        self.cursor = self.conn.cursor()
        sql = 'SELECT `text` FROM abaike_item WHERE word NOT IN (SELECT word FROM abaike_item WHERE word LIKE "%:%")'
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
    sentences = Mysentences_mysql()
    model = gensim.models.Word2Vec(sentences=sentences, size=100, min_count=3)
    model.save(file_path)
    print('cost time: {}'.format(time.time() - start))


def train_tf_idf():
    start = time.time()
    sentences = Mysentences_file(file_path)
    dictionary = gensim.corpora.Dictionary(sentences)
    corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
    model = gensim.models.TfidfModel(corpus)
    model.save(file_path + '.tfidf_model')
    print('cost time: {}'.format(time.time() - start))


# 欧式距离
def euclidSimilar(inA, inB):
    return 1.0 / (1.0 + la.norm(inA - inB))


# 皮尔逊相关系数
def pearsonSimilar(inA, inB):
    if len(inA) < 3:
        return 1.0
    return 0.5 + 0.5 * np.corrcoef(inA, inB, rowvar=0)[0][1]


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


# N个ndarray求平均值
def model_mean(*args):
    # if len(args) != 0:
    #     return sum(args) / len(args)
    return np.mean(args, axis=0)


def get_word_vec(word, model):
    '''
    通过切割word为多个小word，从而找到小word在model的向量表示，进而求平均值，得到大word的向量表示。
    :param word: 待拆分的word
    :param model: word2vec 模型
    :return: word对应model的向量
    '''
    tmp = list()
    word_cut = jieba.cut(word)
    for i in word_cut:
        if i in model:
            vec = model[i]
            tmp.append(vec)
    return word, model_mean(*tmp)


def get_words_vecs(words, model):
    '''
    得到一组词的向量组
    :param words: 一组词
    :param model: word2vec模型
    :return: 一组词对应的向量组
    '''
    words_vecs = list()
    for word in words:
        vec = get_word_vec(word, model)
        words_vecs.append(vec)
    return words_vecs


def map_online_to_icd():
    '''
    线上ICD到标准ICD10的映射
    '''
    path = base_path + 'online_icd/remain_online_icd.xls'
    wb = xlrd.open_workbook(path)
    sheet_online = wb.sheet_by_index(0)
    sheet_icd = wb.sheet_by_index(1)
    online_words = sheet_online.col_values(0)[1:]
    icd_words = sheet_icd.col_values(0)[1:]

    # 随机100个 online_word
    import random
    online_words_random = []
    for i in range(100):
        online_word = random.choice(online_words)
        online_words_random.append(online_word)
    print(len(set(online_words_random)))


    # 加载word2vec模型
    model = gensim.models.Word2Vec.load(file_path_1000_stopwords)
    result = []
    # 计算出所有ICD标准表的词的向量（求平均数）
    icd_vecs = get_words_vecs(icd_words, model)
    online_vecs = get_words_vecs(online_words_random, model)
    # 计算余弦相似度
    for index, (ol_word, ol_vec) in enumerate(online_vecs):
        one_result = []
        for icd_word, icd_vec in icd_vecs:
            similarity = cos_similarity(ol_vec, icd_vec)
            one_result.append((icd_word, similarity))
        # sub_result 降序排序
        one_result.sort(key=lambda x: x[1], reverse=True)
        one_dict = (ol_word, one_result[:5])
        print(index, one_dict)
        result.append(one_dict)
    return result


def use_model():
    # load the original Google word2vec model, use the KeyedVectors.load_word2vec_format()
    model_cbow = gensim.models.KeyedVectors.load_word2vec_format(fname=file_path_baike_cbow, binary=True,
                                                                 encoding='utf-8', unicode_errors='ignore')
    # model_skipgram = gensim.models.KeyedVectors.load_word2vec_format(fname=file_path_baike_skipgram, binary=True, encoding='utf-8', unicode_errors='ignore')
    model_100 = gensim.models.Word2Vec.load(file_path_100)
    model_1000 = gensim.models.Word2Vec.load(file_path_1000)
    model_1000_stopwords = gensim.models.Word2Vec.load(file_path_1000_stopwords)
    # print('你好' in model)
    word = '近视'
    print('100     ', model_100.wv.most_similar(word, topn=5))
    print('1000    ', model_1000.wv.most_similar(word, topn=5))
    print('1000sw  ', model_1000_stopwords.wv.most_similar(word, topn=5))
    print('baike   ', model_cbow.wv.most_similar(word, topn=5))
    # print(model.wv.similarity('中国', '北京'))
    # print(cos_similarity(model['中国'], model['北京']))


def main():
    result = map_online_to_icd()
    result2 = []
    for i in result:    
        a = []
        ol_word = i[0]
        a.append(ol_word)
        result_5 = i[1]
        for ii in result_5:
            icd = ii[0]
            rate = ii[1]
            a.append(icd)
            # a.append(rate)
        result2.append(a)


    # 输出到csv
    with open('online_to_icd_random100.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(('online', 'icd1', 'icd2', 'icd3', 'icd4', 'icd5'))
        f_csv.writerows(result2)


if __name__ == '__main__':
    main()
