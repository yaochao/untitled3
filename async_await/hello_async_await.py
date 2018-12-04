#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/9


import aiohttp
import asyncio
import time

start = time.time()

url = 'https://www.jishux.com'

async def request():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.status


                print(text)
    except Exception as e:
        print(e)


tasks = [asyncio.ensure_future(request()) for _ in range(1000)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('cost:', time.time() - start)
