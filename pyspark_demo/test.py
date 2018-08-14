#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/14


from pyspark import SparkContext


def first():
    sc = SparkContext()
    rdd = sc.textFile('hello.txt')
    c = rdd.filter(lambda line: 'spark' in line).count()
    rdd.saveAsTextFile('saved')
    print(c)


if __name__ == '__main__':
    first()
