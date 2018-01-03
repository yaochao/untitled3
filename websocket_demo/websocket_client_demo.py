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
        # header={'Sec-WebSocket-Extensions':'permessage-deflate; client_max_window_bits'},
        # cookie='__guid=96554777.2769498643221285000.1507102491800.0603; smid=385567c0-b526-49cc-9be1-6aac5745f1e0; R=r%3D3238368%26u%3DCnaqnGi3238368%26n%3D%25R5%25O7%25O4%25R9%25OO%258R%25R5%25N4%259P%25R9%259O%25N8mm%26le%3DrJRyZxRyZxRyZxRyZxR2AFH0ZUSkYzAioD%3D%3D%26m%3DZGtmAwH4Zmp4BQR%3D%26im%3DnUE0pPHmDFHlEvHlEzx1YaOxnJ0hM3ZyZxMzZGD3AQt1ZQMwAmNkLJLkMQAwLmWyMQquAzR2LmL4BP5dpTIa%26p%3D%26i%3D; M=t%3D1512970591%26v%3D1.0%26mt%3D1512970591%26s%3Ddcfa5f2853e20b80a1943bfa80c8ba68; pdft=20171204224557459a3fbc1ff742ca42a53032d3dc4f760106c5c8c131b75b; smidV9=201710041534525edcd7a0a137e8f82ecd96c0e4b8c6bb0075aca434129f28; pdftv1=c72dc|1608d252aa5|43c6|761a4902|f; I=r%3D3238368%26t%3D6e3ac96ab6df9b0ba799f0dc08de6ca5; Hm_lvt_204071a8b1d0b2a04c782c44b88eb996=1513848340,1514196514,1514558638,1514966513; Hm_lpvt_204071a8b1d0b2a04c782c44b88eb996=1514966552'
    )
    ws.on_open = on_open
    ws.run_forever()
