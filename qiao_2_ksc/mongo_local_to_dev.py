#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/17

from qiao_2_ksc import MONGO_CONF, MONGO_CONF2

import pymongo

local_client = pymongo.MongoClient(**MONGO_CONF)
local_db = local_client.get_database('datasets')
local_collection_detail = local_db.get_collection('xam_person_detail_514')

online_client = pymongo.MongoClient(**MONGO_CONF2)
online_db = online_client.get_database('datasets')
online_collection_detail = online_db.get_collection('xam_person_detail_514')


def main():
    result_cursor = local_collection_detail.find()
    counter = 1
    for i in result_cursor:
        online_collection_detail.insert(i)
        counter += 1
        print(counter)


if __name__ == '__main__':
    main()
