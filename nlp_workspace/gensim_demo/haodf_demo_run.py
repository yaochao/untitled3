#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/20


import csv
import time
import jieba
import gensim

# 配置好 logging，gensim 会打印出日志
import logging

import xlrd

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

jieba.load_userdict(f='/Users/yaochao/python/datasets/user_dicts/online_and_icd_and_mesh.txt')
file_path = '/Users/yaochao/python/datasets/haodf_chats_detail_1000W_pre.csv'


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
class Mysentences(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, encoding='utf-8') as f:
            f_csv = csv.reader(f)
            for idx, sentence in f_csv:
                yield list(jieba.cut(sentence))


def train_word2vec():
    start = time.time()
    sentences = Mysentences(file_path)
    model = gensim.models.Word2Vec(sentences=sentences, size=100, min_count=3, workers=10)
    model.save(file_path + '.word2vec_model')
    print('cost time: {}'.format(time.time() - start))


def train_tf_idf():
    start = time.time()
    sentences = Mysentences(file_path)
    dictionary = gensim.corpora.Dictionary(sentences)
    corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
    model = gensim.models.TfidfModel(corpus)
    model.save(file_path + '.tfidf_model')
    print('cost time: {}'.format(time.time() - start))


def use_model():
    model = gensim.models.Word2Vec.load(file_path + '.word2vec_model')
    print(model.wv.most_similar('恶性贫血'))
    model.wv.similarity('中国', '美国')

    # model2 = gensim.models.TfidfModel.load(file_path + '.tfidf_model')
    # sentences = Mysentences(file_path)
    # dictionary = gensim.corpora.Dictionary(sentences)
    # corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
    # corpus_tfidf = model2[corpus]
    # print(corpus_tfidf)


def map_online_to_icd():
    '''
    线上ICD到标准ICD10的映射
    '''
    icd = '/Users/yaochao/Desktop/work_files/work2/ICD.xls'
    online = '/Users/yaochao/Desktop/work_files/work2/online.csv'
    # csv
    csv_reader = csv.reader(open(online, 'r', encoding='utf-8'))
    online_mc = [x[0] for x in csv_reader][1:]
    # xlrd
    icd = xlrd.open_workbook(icd)
    sheet = icd.sheet_by_index(1)
    icd_mc = sheet.col_values(1)[1:]

    # 加载word2vec模型
    model = gensim.models.Word2Vec.load(file_path + '.word2vec_model')
    result = []
    for online_word in online_mc[:1]:
        sub_result = []
        for icd_word in icd_mc:
            try:
                similarity = model.wv.similarity(online_word, icd_word)
                sub_result.append((similarity, icd_word))
            except Exception as e:
                pass

        # sub_result 排序
        sub_result.sort(key=lambda x: x[0], reverse=True)
        result.append((sub_result, online_word))
    print(result)


if __name__ == '__main__':
    train_word2vec()
    # map_online_to_icd()
    # use_model()
    # train_tf_idf()
