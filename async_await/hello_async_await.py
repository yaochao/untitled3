#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/9


import aiohttp
import asyncio
import time

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    text = await response.text()
    return text


async def request():
    url = 'http://127.0.0.1:5000/'
    text = await get(url)
    print(text)


tasks = [asyncio.ensure_future(request()) for _ in range(8)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('cost:',time.time() - start)

