#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/14


from pyspark import SparkContext

sc = SparkContext()
rdd = sc.textFile('file:///Users/yaochao/python/PycharmProjects/untitled3/pyspark_demo/word.txt')
rdd = rdd.flatMap(lambda line: line.split(' ')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).foreach(print)
# wordcount = rdd.collect()
# print(wordcount)
