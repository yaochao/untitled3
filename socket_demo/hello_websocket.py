#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/7/3


import websockets
import asyncio


async def hello():
    async with websockets.connect('wss://tweetyf.org/wsvote') as websocket:
        msg = '{"a":"vote_p","pid":3274,"m":"con"}'
        for i in range(10000):
            await websocket.send(msg)
            # response = await websocket.recv()
            print(i)


def main():
    asyncio.get_event_loop().run_until_complete(hello())


if __name__ == '__main__':
    main()
