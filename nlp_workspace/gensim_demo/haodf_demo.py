#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/20


import csv
import time
import jieba
import gensim


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
            for id, sentence in f_csv:
                yield list(jieba.cut(sentence))


file_path = '/Users/yaochao/python/corpus/haodf_chats_detail_100W_pre.csv'


def train_model():
    start = time.time()
    sentences = Mysentences(file_path)
    model = gensim.models.Word2Vec(sentences=sentences, size=100, min_count=5, workers=3)
    model.save(file_path + '.model')
    print('cost time: {}'.format(time.time() - start))


def use_model():
    model = gensim.models.Word2Vec.load(file_path + '.model')
    print(model.most_similar('发烧'))


if __name__ == '__main__':
    # train_model()
    use_model()
