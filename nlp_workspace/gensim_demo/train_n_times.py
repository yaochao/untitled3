#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/22


import gensim
from gensim import corpora
import jieba
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# with open('/Users/yaochao/test/nlp/a.txt', 'r', encoding='utf-8') as f:
#     text = f.readline()
# print(text)
# sentences = [jieba.cut(s) for s in text]

class Sentences(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open('/Users/yaochao/test/nlp/a.txt', 'r', encoding='utf-8') as f:
            text = f.readlines()
            for s in text:
                yield list(jieba.cut(s))

def get_corpus():
    sentences = Sentences('/Users/yaochao/test/nlp/a.txt')
    corpus = [corpora.Dictionary(sentence) for sentence in sentences]
    print(corpus)


def train_first():
    sentences = Sentences(path='/Users/yaochao/test/nlp/a.txt')
    model = gensim.models.Word2Vec(sentences, min_count=2)
    # model.save('/Users/yaochao/test/nlp/first.model')

def train_iter(text_path, model_path):
    sentences = Sentences(text_path)
    model = gensim.models.Word2Vec.load(model_path)
    model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
    model.save(model_path)


def test_model(path):
    model = gensim.models.Word2Vec.load(path)
    w = model.most_similar('中国')
    print(w)

if __name__ == '__main__':
    text_path = '/Users/yaochao/test/nlp/b.txt'
    model_path = '/Users/yaochao/test/nlp/first.model'

    # # 迭代训练
    # train_iter(text_path, model_path)
    #
    # # 测试
    # test_model(model_path)

    get_corpus()