#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/7


import socket
import time

HOST = '127.0.0.1'
PORT = 12349


class SServer(object):
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.new_conn = None

    def start(self):
        self.socket.listen(5)  # TODO backlog的作用
        print('SServer started at {}:{}'.format(self.host, self.port))
        new_conn, client_addr = self.socket.accept()
        self.new_conn = new_conn
        print('Connected by {}'.format(client_addr))

        while True:
            data = self.new_conn.recv(1024)
            data = data.decode('utf-8')
            print(data)
            self.new_conn.send('server received: {}'.format(data).encode('utf-8'))

    def __del__(self):
        print('__del__')
        self.socket.close()
        if hasattr(self, 'new_conn'):
            self.new_conn.close()


class SClient(object):
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, msg):
        self.socket.send(msg)
        data = self.socket.recv(1024)
        print(data)

    def __del__(self):
        print('__del__')
        self.socket.close()

if __name__ == '__main__':
    client = SClient()
    for i in range(10):
        client.send(b'This is {}'.format(i).encode('utf-8'))
        time.sleep(1)
