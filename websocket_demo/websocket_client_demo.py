#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/1/3


import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(ws, message):
    print('on_message:', message)


def on_error(ws, error):
    print('on_error:', error)


def on_data(ws, data):
    print('on_data:', data)


def on_close(ws):
    print('on_close:', "### closed ###")


def on_open(ws):
    print('on_open:', "### opened ###")
    # ws.send(b'open')
    # def run(*args):
    #     for i in range(3):
    #         time.sleep(1)
    #         ws.send("Hello %d" % i)
    #     time.sleep(1)
    #     ws.close()
    #     print("thread terminating...")
    #
    # thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://wangsu-bjac.gw.riven.panda.tv/",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_data=on_data,
    )
    ws.on_open = on_open
    ws.run_forever()
