#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/4/19



import pymongo
from collections import Counter
import jieba

MONGO_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
}
client = pymongo.MongoClient(**MONGO_CONFIG)
db = client['datasets']
collection_list = db['xam_person_list']
collection_detail = db['xam_person_detail']


def get_all_name():
    cursor = collection_list.find({}, {'P_NAME': 1, '_id': 0})
    result = list(cursor)
    names = [i['P_NAME'] for i in result]
    words = []
    for name in names:
        # name = list(name) # 分为单个的字
        name = jieba.cut(name)
        words += name
    counter = Counter(words)
    a = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    print(a[:100])


if __name__ == '__main__':
    get_all_name()
