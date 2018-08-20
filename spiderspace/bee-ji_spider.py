#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/15
import time

import aiohttp
import asyncio
import pymongo

MONGOCOF = {
    'host': '127.0.0.1',
    'port': 27017
}

client = pymongo.MongoClient(**MONGOCOF)


async def request(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status == 200:
            return await response.json()


def callback(future):
    try:
        db = client.get_database('datasets')
        collection = db.get_collection('bee-ji')
        result = future.result()
        for i in result:
            i['_id'] = i['id']
            collection.insert_one(i)
            print('success')
    except Exception as e:
        pass


def main():
    start = time.time()
    url = 'http://www.bee-ji.com:9000/search/json'
    tasks = [asyncio.ensure_future(request(url)) for _ in range(1000)]
    [task.add_done_callback(callback) for task in tasks]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print('cost:', time.time() - start)


if __name__ == '__main__':
    main()
