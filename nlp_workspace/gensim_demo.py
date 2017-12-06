#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/10

from gensim.models import word2vec

# 加载语料库
sentences = word2vec.Text8Corpus('dicts_illness.txt')
model = word2vec.Word2Vec(sentences=sentences, size=200)
print(model)