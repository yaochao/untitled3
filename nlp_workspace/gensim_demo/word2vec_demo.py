#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/17

# https://zhuanlan.zhihu.com/p/24961011

import gensim
from gensim.models import word2vec
import logging
import os
import jieba

# 引入日志配置
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# # 引入数据集
# raw_sentences = ["the quick brown fox jumps over the lazy dogs", "yoyoyo you go home now to sleep"]
#
# # 分词 list of list: 一个包含分过词（分词列表）的句子的列表 [[我, 爱, 中国], [你们,好]]
# sentences = [s.split() for s in raw_sentences]
#
# # 构建模型 model
# # min_count: 代表可接受的词的最小词频，小于这个值的词不会被训练，默认5
# # size: 代表神经网络层数，默认100
# # workers: 代表并行训练的线程数，默认为3 （当Cython安装的情况下才起作用？？）
# model = word2vec.Word2Vec(sentences=sentences, min_count=1, size=100, workers=3)
# # 构建模型 第二种操作: 把上面的一步操作分开两步：构造词表，训练模型
# model = gensim.models.Word2Vec(iter=1)  # an empty model, no training yet
# model.build_vocab(sentences)  # can be a non-repeatable, 1-pass generator
# model.train(sentences)  # can be a non-repeatable, 1-pass generator
#
# # 进行相关性比较
# print(model.similarity('dogs', 'you'))


# 引入语料库
# 对于大量的输入语料库或者需要整合磁盘多个文件的数据，应该使用迭代器(iterator)方式，避免内存被撑爆
class Mysentences(object):
    def __init__(self, dirname, chs=True):
        self.dirname = dirname
        self.chs = chs

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for sentence in open(os.path.join(self.dirname, fname), encoding='utf-8'):
                # 对 sentence 做分词，英语直接split分词，中文用 jieba 分词
                if self.chs:
                    yield list(jieba.cut(sentence=sentence))
                else:
                    yield sentence.split()
sentences = Mysentences(dirname='/Users/yaochao/test/w2v', chs=True)
model = gensim.models.Word2Vec(sentences, min_count=1)
print(model.most_similar('中国'))
print(model.doesnt_match('中国'))
print(model.similarity('中国', '较强'))
print(model['中国'])

# # 模型的保存与读取
# # 保存1
# model.save('test.model') # 后缀名随便写给人看的，其实是个二进制文件，不写后缀也可以
# # 读取1
# model = gensim.models.Word2Vec.load('test.model')
# # 保存2 (保存成word2vec兼容的model，其他（语言/库）实现的word2vec随便使用)
# model.wv.save_word2vec_format('test.model.bin') # 后缀名随便写给人看的，一个二进制文件，不写后缀也可以
# # 读取2
# model = gensim.models.KeyedVectors.load_word2vec_format('test.model.bin')

# 模型的评估
# 格式：每一条遵循A is to B as C is to D这个格式
model.accuracy('这里应该是一个标准的文件，格式与questions-words.txt相同')