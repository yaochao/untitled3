#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/6/11


import pymongo

MONGO_CONF = {
    'host': '127.0.0.1',
    'port': 27017,
}

MONGO_CONF2 = {
    'host': '127.0.0.1',
    'port': 27018,
}


def transfer_data():
    client = pymongo.MongoClient(**MONGO_CONF)
    client2 = pymongo.MongoClient(**MONGO_CONF2)
    collection = client.get_database('datasets').get_collection('xam_person_list_518')
    collection2 = client2.get_database('datasets').get_collection('xam_person_list_518')

    cursor = collection2.find()
    counter = 0
    for item in cursor:
        collection.insert(item)
        counter += 1
        print('已完成{}个'.format(counter))


if __name__ == '__main__':
    transfer_data()
