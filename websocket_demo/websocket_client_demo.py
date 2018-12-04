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


def on_data(ws, data, data_type, flag):
    print('on_data:', data)
    print('data_type:', data_type)
    print('flag:', flag)
    if flag:
        time.sleep(25)
        ws.send("2")


def on_close(ws):
    print('on_close:', "### closed ###")


def on_open(ws):
    print('on_open:', "### opened ###")
    ws.send("2probe")
    time.sleep(1)
    ws.send("5")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        url="wss://sshibkhhjk.jin10.com:8081/socket.io/?EIO=3&transport=websocket",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_data=on_data,
        header={"Origin": "https://www.jin10.com"}
    )
    ws.on_open = on_open
    ws.run_forever()
